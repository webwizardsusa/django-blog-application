from django.db import models
from django.utils.text import slugify

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, max_length=255, null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    class Meta:
        db_table = 'tags'

    def __str__(self):
        return self.name
