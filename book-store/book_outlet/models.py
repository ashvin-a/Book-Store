from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
# Create your models here.

class Book (models.Model):

    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    author = models.CharField(null=True,max_length=100)
    is_bestselling = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title},{self.rating},{self.author},{self.is_bestselling}"
    
    def get_url(self):
        return reverse("book_detail",args=[self.id])