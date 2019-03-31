from django.db import models

class Translation(models.Model):
    original = models.CharField(max_length=200)
    translation = models.CharField(max_length=200)
