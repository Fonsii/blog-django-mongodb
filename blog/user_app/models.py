from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=300)
    author = models.CharField(max_length=20)
    created_at = models.DateField()
    photo = models.ImageField(upload_to='post/covers', default='post/covers/default.png')

