import random
from faker import Faker
from django.core.management.base import BaseCommand
from web_admin.post.models import Post, Category

class Command(BaseCommand):
    help = "Generate fake categories and posts"

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create fake categories
        self.stdout.write("Generating categories...")
        categories = []
        for _ in range(6):
            category = Category.objects.create(
                name=fake.word().capitalize(),
                description=fake.sentence()
            )
            categories.append(category)

        self.stdout.write(f"{len(categories)} categories created.")

        # Create fake posts
        self.stdout.write("Generating posts...")
        for _ in range(50):
            Post.objects.create(
                title=fake.sentence(nb_words=6),
                content=fake.text(max_nb_chars=1000),
                is_published=1,
                category=random.choice(categories),
            )

        self.stdout.write("Fake data generation completed.")
