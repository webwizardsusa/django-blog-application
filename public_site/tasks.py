from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

@shared_task
def send_contact_email_task(subject, message, from_email, recipient_list):
    send_mail(subject, message, from_email, recipient_list)

@shared_task
def send_register_email(username, email, login_url):
    """Sends the registration confirmation email asynchronously."""
    context = {
        "user_name": username,
        "user_email": email,
        "login_url": login_url
    }
    
    html_content = render_to_string("public_site/register_email.html", context)
    text_content = strip_tags(html_content)

    email_message = EmailMultiAlternatives(
        subject="Registration Successful",
        body=text_content,
        from_email="admin@example.com",
        to=[email]
    )
    email_message.attach_alternative(html_content, "text/html")
    email_message.send()