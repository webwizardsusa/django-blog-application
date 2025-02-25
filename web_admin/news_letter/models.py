from django.db import models
from django.contrib.auth.models import User, Group
from ckeditor.fields import RichTextField

# Create your models here.
class NewsLetter(models.Model):
    title = models.TextField(max_length=255)
    subject = models.TextField(max_length=255)
    content = RichTextField()
    status = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news_letters', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_news_letters')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'news_letters'
        
    def __str__(self):
        return self.title