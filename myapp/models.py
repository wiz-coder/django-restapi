from django.db import models
from datetime import datetime

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    published = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

        class Meta:
            ordering = ['-published']
