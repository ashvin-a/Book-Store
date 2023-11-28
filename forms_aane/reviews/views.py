from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
# Create your views here.
def reviews(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data        
            print(data)
            return HttpResponseRedirect("/thankuu")
    
    form = ReviewForm()
    
    return render(request,"reviews/reviews.html",{
        "form":form
    })

def thanku(request):
    return render(request,"reviews/thank_you.html")