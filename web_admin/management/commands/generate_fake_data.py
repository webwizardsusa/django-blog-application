import random
from faker import Faker
from django.core.management.base import BaseCommand
from web_admin.blog.models import Blog, Category

class Command(BaseCommand):
    help = "Generate fake categories and blog posts"

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

        # Create fake blog posts
        self.stdout.write("Generating posts...")
        for _ in range(50):
            Blog.objects.create(
                title=fake.sentence(nb_words=6),
                content=fake.text(max_nb_chars=1000),
                is_published=1,
                category=random.choice(categories),
            )

        self.stdout.write("Fake data generation completed.")
