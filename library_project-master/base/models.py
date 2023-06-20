from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)
    image = models.URLField()
    description = models.TextField(null=True)
    language = models.CharField(max_length=255, null=True)
    category = models.CharField(max_length=255, null=True)
    reserved = models.BooleanField(default=False)
    reserved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title