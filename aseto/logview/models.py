from django.db import models
from django.utils import timezone


class LogEntry(models.Model):
    filename = models.CharField(max_length=250)
    timestamp = models.DateTimeField(default=timezone.now)
    message = models.TextField()

    def __str__(self):
        return str(f'{self.filename} | {self.timestamp} | {self.message}')
