from django.db import models
from web_admin.category.models import Category
from web_admin.tag.models import Tag
from django.contrib.auth.models import User
from django.utils.text import slugify

class Post(models.Model):
    DRAFT = False
    PUBLISHED = True

    STATUS_CHOICES = [
        (DRAFT, "Draft"),
        (PUBLISHED, "Published"),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255, null = True, blank = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    is_published = models.BooleanField(default=True)
    published_at = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name='posts')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'posts'

    def __str__(self):
        return self.title
