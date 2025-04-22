from django.core.management.base import BaseCommand
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.utils.timezone import now
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.urls import reverse
from web_admin.post.models import Post
from public_site.models import Subscriber
import re

class Command(BaseCommand):
    help = "Check and publish scheduled posts based on date (ignoring time)"

    def clean_content(self, content):
        """Clean HTML content and format it properly."""
        text = strip_tags(content)
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'\n\s*\n', '\n\n', text)
        if len(text) > 200:
            text = text[:197] + '...'
        return text.strip()

    def send_notification_email(self, post, subscriber_email):
        """Send a beautiful HTML email to a subscriber about the new post."""
        context = {
            'post_title': post.title,
            'post_excerpt': self.clean_content(post.content),
            'post_url': f"{settings.SITE_DOMAIN}{reverse('post_detail', kwargs={'slug': post.slug})}",
            'author_name': post.author.get_full_name(),
            'unsubscribe_url': f"https://python.webwizardsusa.com/unsubscribe/?email={subscriber_email}"
        }

        html_content = render_to_string('public_site/new_post_notification.html', context)
        text_content = strip_tags(html_content)

        subject = f"New Blog Post: {post.title}"
        email = EmailMultiAlternatives(subject=subject, body=text_content, from_email=settings.DEFAULT_FROM_EMAIL, to=[subscriber_email])
        email.attach_alternative(html_content, "text/html")
        
        try:
            email.send()
            return True
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Failed to send email to {subscriber_email}: {str(e)}"))
            return False

    def handle(self, *args, **kwargs):
        today = now().date()

        scheduled_posts = Post.objects.filter(is_published=True, published_at=today).select_related("author")  

        if not scheduled_posts.exists():
            self.stdout.write(self.style.WARNING("No posts to send emails for at this time."))
            return

        subscribers = Subscriber.objects.filter(is_active=True)
        
        if not subscribers.exists():
            self.stdout.write(self.style.WARNING("No active subscribers found."))
            return

        for post in scheduled_posts:
            subject = f"Your Blog Post Has Been Published: {post.title}"
            message = f"Your blog post has been published:\n\nTitle: {post.title}\n\nView it here: {settings.SITE_DOMAIN}{reverse('post_detail', kwargs={'slug': post.slug})}"
            try:
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [post.author.email], fail_silently=False)
                self.stdout.write(self.style.SUCCESS(f"Author notification sent for post: {post.title}"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Failed to send author notification for {post.title}: {str(e)}"))

            successful_sends = 0
            for subscriber in subscribers:
                if self.send_notification_email(post, subscriber.email):
                    successful_sends += 1

            self.stdout.write(
                self.style.SUCCESS(
                    f"Post '{post.title}' notification sent to {successful_sends} out of {subscribers.count()} subscribers"
                )
            )
