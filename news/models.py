from django.db import models

from techNews import settings


# Create your models here.

class Topic (models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Content(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    cover_image = models.ImageField(null=True, blank=True)
    tags = models.ManyToManyField(Topic, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def is_replied(self):
        return self.parent is not None

