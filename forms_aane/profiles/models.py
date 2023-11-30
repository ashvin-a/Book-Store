from django.db import models

# Create your models here.

class ProfileModel(models.Model):
    image = models.FileField(upload_to='images')