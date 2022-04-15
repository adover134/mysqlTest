from django.db import models
from django_mysql.models import ListTextField


class User(models.Model):
    name = models.TextField()
    childrenNames = ListTextField(
        base_field=models.CharField(max_length=30),
        size=5
    )
    pointNumbers = models.JSONField()
