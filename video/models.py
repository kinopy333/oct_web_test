from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=100)
    videofile = models.FileField(upload_to='videos/',
     null=True, verbose_name='video_image', blank=False)

    def __str__(self):
        return self.title

class Review(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    #name = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='User name', max_length=20)
    video_class = (
        ('rp', 'ruptured plaque'), 
        ('er', 'erosion'),
        ('cn', 'calcified nodule'), 
        ('none', 'no vulanable plaque'), 
        ('in', 'indistinguishable'),
    )
    body = models.CharField(verbose_name='Classification', max_length=20, 
    choices = video_class, default='rp')
    
    def __str__(self):
        return self.name