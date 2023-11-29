from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .forms import ReviewForm

# Create your views here.

class ReviewView(View):
    
    def post(self,request):
        form = ReviewForm(request.POST)
        if form.is_valid():  
            form.save()         
            return HttpResponseRedirect("/thankuu")
        return render(request,"reviews/reviews.html",{
        "form":form
    })
    
    def get(self,request):
        form = ReviewForm()
        return render(request,"reviews/reviews.html",{
        "form":form
    })

class ThankuView(View):
    
    def get(self,request):
        return render(request,"reviews/thank_you.html")