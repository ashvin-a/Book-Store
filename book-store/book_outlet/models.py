from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.IntegerField(validators=[MinValueValidator(1),
                                           MaxValueValidator(100)])

    class Meta:
        verbose_name_plural = "Countries"
        
    def __str__(self) -> str:
        return f"{self.name}"        

class Address(models.Model):
    house_no = models.CharField(max_length=20)
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.house_no}, {self.street}, {self.city}"
    
    class Meta:
        verbose_name_plural = "Address Entries" #How to override Addresss
    
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.OneToOneField(Address,on_delete=models.CASCADE,
                                   null=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Book (models.Model):

    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1),
                                             MaxValueValidator(5)])
    author = models.ForeignKey(Author,on_delete=models.CASCADE,
                               null=True,related_name="books")
    country = models.ManyToManyField(Country)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="",blank=True,null=False,db_index=True)

    def __str__(self):
        return f'''{self.title},{self.rating},{self.author},
                {self.is_bestselling}'''

    def get_url(self):
        return reverse("book_detail",args=[self.slug])