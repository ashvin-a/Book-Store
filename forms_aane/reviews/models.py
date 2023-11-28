from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
class Review(models.Model):
    username = models.CharField(max_length=100)
    review_text = models.TextField(max_length=500)
    rating = models.IntegerField(validators=[MinValueValidator(1),
                                             MaxValueValidator(10)])