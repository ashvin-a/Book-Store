from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
def reviews(request):
    if request.method == 'POST':
        data = request.POST["username"]
        print(data)
        return HttpResponseRedirect("/thankuu")
    return render(request,"reviews/reviews.html")

def thanku(request):
    return render(request,"reviews/thank_you.html")