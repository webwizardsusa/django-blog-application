from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    subject = models.TextField(null=True)
    message = models.TextField()


    class Meta:
        db_table = 'contacts'

    def __str__(self):
        return self.first_name