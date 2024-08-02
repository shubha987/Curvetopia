# whiteboard/models.py
from django.db import models

class Polyline(models.Model):
    data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
