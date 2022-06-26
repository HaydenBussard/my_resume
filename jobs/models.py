from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=400)
    
    def __str__(self):
        return self.summary


class Header(models.Model):
    name = models.CharField(max_length=20)
    summary = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/')