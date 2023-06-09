from django.db import models
from django.contrib.auth.models import User

from taggit.managers import TaggableManager


class Post(models.Model):
    title = models.CharField(max_length=200, null=False)
    content = models.TextField(null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200)
    tags = TaggableManager(blank=True)

    class Meta:
        ordering = ['-date_published']
    
    def __str__(self):
        return self.title
    