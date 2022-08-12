from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=300)
    author = models.CharField(max_length=20)
    created_at = models.DateField()
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
