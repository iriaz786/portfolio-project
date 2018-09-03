from django.db import models

# Create your models here.
class Blog(models.Model):
    image=models.ImageField(upload_to='images/')
    title=models.CharField(max_length=255)
    pub_date=models.DateTimeField(max_length=20)
    body=models.TextField(max_length=500)
    image=models.ImageField(upload_to='images/')
