from django.db import models
# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now) 
    #auto_now = True -> changes everytime update
    #auto_now_add = True -> time when object was created (can never update the value of date_posted)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - {self.author}'
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})