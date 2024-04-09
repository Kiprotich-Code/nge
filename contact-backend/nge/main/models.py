from django.db import models

# Create your models here.
# Store Mailing List 
class WaitList(models.Model):
    email = models.EmailField()
    message = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f'Message from: {self.email}!'