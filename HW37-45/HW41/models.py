# models.py
from django.db import models

class MyModel(models. Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/') # Изображения будут сохраняться в 'media/images/"