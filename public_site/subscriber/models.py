from django.db import models
from web_admin.news_letter.models import NewsLetter

# Create your models here.
class Subscriber(models.Model):
    
    email = models.EmailField(max_length=254)
    news_letter = models.ForeignKey(NewsLetter, on_delete=models.CASCADE, related_name='subscribers', null=True)
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'subscribers'

    def __str__(self):
        return self.email