from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
# Create your views here.
def reviews(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = Review(username=form.cleaned_data['username'],
                            review_text=form.cleaned_data['review_text'],
                            rating=form.cleaned_data['rating'])   
            review.save()         
            return HttpResponseRedirect("/thankuu")
    else:
        form = ReviewForm()
    
    return render(request,"reviews/reviews.html",{
        "form":form
    })

def thanku(request):
    return render(request,"reviews/thank_you.html")