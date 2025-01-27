from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tags'

    def __str__(self):
        return self.name
    
    def get_created_at(self):
        return self.created_at.strftime('%m/%d/%Y')