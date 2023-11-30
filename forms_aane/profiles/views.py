from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
# Create your views here.

def store_file(file):
    with open('temp/output.jpg','wb+') as dest:
        for chunk in file.chunks():
            dest.write(chunk)
            
class CreateProfileView(View):
    def get(self, request):
        return render(request, "profiles/create_profile.html")

    def post(self, request):
        store_file(request.FILES['image']) #FILES gets the data from form
        return HttpResponseRedirect("/profiles")