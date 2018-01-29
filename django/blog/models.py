from django.db import models

# Create your models here.
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    create_date = models.DateTimeField(
        default=timezone.new
    )
    published_Date = models.DateTimeField(
        blank=True, null=True
    )

    def publish(self):
        self.published_date = timezone.new()
        self.save()

    def __str__(self):
        return self.self