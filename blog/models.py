from django.db import models

# Create your models here.
class Blog(models.Model):
    image=models.ImageField(upload_to='images/')
    title=models.CharField(max_length=255)
    pub_date=models.DateTimeField(max_length=20)
    body=models.TextField(max_length=500)
    image=models.ImageField(upload_to='images/')

#function to show title in the list of blogs

    def __str__(self):
        return self.title


#function to reduce the size of the summary
    def summary(self):
        return self.body[:100]
#function to fomrat the date Also use of the strftime from strftime.org
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
