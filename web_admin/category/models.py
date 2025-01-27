from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name