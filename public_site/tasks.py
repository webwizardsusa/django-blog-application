from celery import shared_task
from django.core.mail import send_mail
from blog_application import settings
from web_admin.news_letter.models import NewsLetter
from public_site.subscriber.models import Subscriber
from django.template.loader import render_to_string
from django.db import connection

@shared_task
def send_contact_email_task(subject, message, from_email, recipient_list):
    send_mail(subject, message, from_email, recipient_list)
    
@shared_task
def send_news_letter_task():
    news_letter = NewsLetter.objects.filter(status=0).first()
    if news_letter:
        subscribers_email = Subscriber.objects.exclude(news_letter_id = news_letter.pk).filter(status=0).values_list('email', flat=True)[:9]
        if subscribers_email:
            connection.close()
            Subscriber.objects.filter(email__in = list(subscribers_email)).update(status=1, news_letter_id=news_letter.pk)
            
            subject = news_letter.subject
            message = news_letter.content
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = list(subscribers_email)
            
            context = {
                "newsletter": news_letter,
                "recipient": recipient_list,
            }
            html_message = render_to_string("public_site/emails/news_letter_template.html", context)

            # Call the Celery task to send the email asynchronously
            send_mail(subject, message, from_email, recipient_list, fail_silently=False, html_message=html_message)
        else:
            NewsLetter.objects.filter(id=news_letter.id).update(status=1)
            Subscriber.objects.filter(news_letter_id = news_letter.pk).update(status=0)
    else:
        return "No new news letters"   