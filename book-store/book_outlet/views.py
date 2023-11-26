from django.shortcuts import render
from .models import Book
# Create your views here.

def index(request):
    book = Book.objects.all()
    return render(request,"book_outlet\index.html",{
        "books":book
    })

def book_detail(request,slug):
    book = Book.objects.get(slug=slug)
    return render(request,"book_outlet\ook_detail.html",{
        "title":book.title,
        "author":book.author,
        "rating":book.rating,
        "is_bestselling":book.is_bestselling
    })

