from django.db import models
from django.utils import timezone


class Item(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now,  )

# Create your models here.
