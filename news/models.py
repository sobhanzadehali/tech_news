from django.db import models
from django.contrib.auth.models import User
from techNews import settings



# Create your models here.

class Topic (models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Content(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    cover_image = models.ImageField(null=True, blank=True)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    topics = models.ManyToManyField(Topic, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    likes = models.ManyToManyField(User, blank=True, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def is_replied(self):
        return self.parent is not None

    def __str__(self):
        return self.body

