from django.db import models


class Log(models.Model):
    ip = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
