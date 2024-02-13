from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=800)
