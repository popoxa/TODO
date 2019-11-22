from django.conf import settings
from django.db import models
from django.utils import timezone

class Case(models.Model):
    text_case = models.CharField(max_length=40)
    complete_case = models.BooleanField(default=False)

    def __str__(self):
        return self.text_case

# Create your models here.
