from django.contrib import admin
from .models import Post,Author,Tag
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name")

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
     
    
admin.site.register(Post,PostAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Tag)