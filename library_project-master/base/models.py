from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)
    image = models.URLField()
    description = models.TextField(null=True)
    language = models.CharField(max_length=255, null=True)
    category = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title