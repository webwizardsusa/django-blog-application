from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings
from django.utils.timezone import now
from web_admin.post.models import Post

class Command(BaseCommand):
    help = "Check and publish scheduled posts based on date (ignoring time)"

    def handle(self, *args, **kwargs):
        today = now().date()

        scheduled_posts = Post.objects.filter(is_published=True, published_at=today).select_related("author")  

        for post in scheduled_posts:
            subject = f"New Blog Post Published: {post.title}"
            message = f"A new blog post has been published:\n\nTitle: {post.title}\n\nRead it here: https://python.webwizardsusa.com/posts/{post.slug}/"
            recipient_list = [post.author.email]
            try:
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list, fail_silently=False,)
                self.stdout.write(self.style.SUCCESS(f"Email sent for post: {post.title}"))

            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Failed to send email for {post.title}: {str(e)}"))

        if not scheduled_posts.exists():
            self.stdout.write(self.style.WARNING("No posts to send emails for at this time."))
