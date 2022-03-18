from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

class post(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    extract = models.CharField(max_length=1000)
    date_pub = models.DateTimeField()
    author = models.CharField(max_length=250, default='Javier Yance')
    created_at = models.DateTimeField(auto_now_add=True)

