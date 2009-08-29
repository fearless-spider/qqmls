from django.db import models
from django.contrib.auth.models import User


class Entry(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateField(None, None, True, True)
    created_by = models.ForeignKey(User)
    status = models.IntegerField()
