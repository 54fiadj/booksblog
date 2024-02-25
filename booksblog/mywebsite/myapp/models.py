from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    rating = models.FloatField()
    review = models.TextField()
    picture = models.ImageField(upload_to='book_pictures/', null=True, blank=True)

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='blog_thumbnails/', blank=True, null=True)

