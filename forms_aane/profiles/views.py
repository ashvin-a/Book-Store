from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import ProfileModel
# Create your views here.

class CreateProfileView(View):
    
    def get(self, request):
        form = ProfileForm
        return render(request, "profiles/create_profile.html",{
            "form":form
        })

    def post(self, request):
        
        submitted_form = ProfileForm(request.POST,request.FILES)
        
        if submitted_form.is_valid():
            profile = ProfileModel(image = request.FILES['image']) #FILES gets the data from form
            profile.save()
            return HttpResponseRedirect("/profiles")
        
        else:
            return render(request,"profiles/create_profile.html",{
            "form": submitted_form
        })