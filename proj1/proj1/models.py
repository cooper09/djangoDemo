# models.py
from django.db import models

class table1(models.Model):
    field1   = models.CharField(max_length=200)