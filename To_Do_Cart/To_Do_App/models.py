from django.db import models
from django.utils import timezone


class Todo(models.Model):
    added_date = models.DateField(default=timezone.now)
    text = models.CharField(max_length=50)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.text
