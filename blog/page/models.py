from django.db import models
from django.urls import reverse
# Create your models here.

class Tag(models.Model):
    
    caption = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return f"{self.caption}"

class Author(models.Model):
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
class Post(models.Model):
    
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=50)
    image_name = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(default="",blank=True,null=False,db_index=True)
    content = models.TextField(max_length=500,default="")
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True)
    tag = models.ManyToManyField(Tag)
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def get_url(self):
        return reverse('blog_detail',args=[self.slug])
    

