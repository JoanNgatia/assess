from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Book(models.Model):
    """Models for books in the libary."""

    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    read = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
