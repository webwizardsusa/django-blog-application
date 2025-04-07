from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

@shared_task
def send_registration_email(username, email, login_url):
    """Sends the registration confirmation email asynchronously."""
    context = {
        "author_name": username,
        "author_email": email,
        "login_url": login_url
    }
    
    html_content = render_to_string("email.html", context)
    text_content = strip_tags(html_content)

    email_message = EmailMultiAlternatives(
        subject="Registration Successful - Awaiting Activation",
        body=text_content,
        from_email="admin@example.com",
        to=[email]
    )
    email_message.attach_alternative(html_content, "text/html")
    email_message.send()
