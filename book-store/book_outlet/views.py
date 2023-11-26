from django.shortcuts import render
from .models import Book
from django.db.models import Avg
# Create your views here.

def index(request):
    book = Book.objects.all().order_by("title")
    num_books = book.count()
    avg_rating = book.aggregate(Avg("rating"))
    return render(request,"book_outlet\index.html",{
        "books":book,
        "total":num_books,
        "avg_rating":avg_rating
    })

def book_detail(request,slug):
    book = Book.objects.get(slug=slug)
    return render(request,"book_outlet\ook_detail.html",{
        "title":book.title,
        "author":book.author,
        "rating":book.rating,
        "is_bestselling":book.is_bestselling
    })

