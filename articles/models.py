from django.db import models
from django.conf import settings

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)
