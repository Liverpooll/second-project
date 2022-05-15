from django.db import models
from common.models import TimeStampedModel


class Post(TimeStampedModel):
    title = models.CharField(max_length=20)
    content = models.TextField()

    def __str__(self):
        return self.title
