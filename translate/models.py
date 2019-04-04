from django.db import models

class Translation(models.Model):
    original = models.CharField(max_length=200)
    translation = models.CharField(max_length=200)
    target_language = models.CharField(max_length=5)
    source_language = models.CharField(max_length=5)
