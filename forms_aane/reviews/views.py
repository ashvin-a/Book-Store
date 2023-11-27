from django.shortcuts import render

# Create your views here.
def reviews(request):
    return render(request,'reviews/reviews.html')