from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100,default="")
    image = models.ImageField(upload_to='images/')
    summary=models.CharField(max_length=200)
    url = models.URLField(max_length=200,default="")

class Contact(models.Model):
        name = models.CharField(max_length=200)
        from_email = models.EmailField()
        subject = models.CharField(max_length=800)
        message = models.TextField(blank=False)

        def __str__(self):
            return self.name