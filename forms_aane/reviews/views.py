from typing import Any
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView,FormView,CreateView
from .forms import ReviewForm
from .models import Review

# Create your views here.

# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/reviews.html"
#     success_url = "/thankuu"
    
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
    #OR
class ReviewView(CreateView):
    form_class = ReviewForm
    model = Review
    template_name = "reviews/reviews.html"
    success_url = "/thankuu"
    
    
class ThankuView(TemplateView):
    template_name="reviews/thank_you.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "BLAHHHH!"
        return context
    

class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"
    
class DetailedView(DetailView):
    template_name = "reviews/details.html"
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        fav_id = request.session.get('favourite_review')
        context['is_favourite'] = (str(fav_id) == str(loaded_review.id))
        return context

class AddFavourite(View):
    def post(self,request):
        review_id = request.POST['review_id']
        request.session['favourite_review'] = review_id
        return HttpResponseRedirect("/review/"+review_id)
# class ReviewView(View):
    
#     def post(self,request):
#         form = ReviewForm(request.POST)
#         if form.is_valid():  
#             form.save()         
#             return HttpResponseRedirect("/thankuu")
#         return render(request,"reviews/reviews.html",{
#         "form":form
#     })
    
#     def get(self,request):
#         form = ReviewForm()
#         return render(request,"reviews/reviews.html",{
#         "form":form
#     })
    
# class ReviewListView(TemplateView):
#     template_name="reviews/review_list.html"
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context
    
# class DetailedView(TemplateView):
#     template_name = "reviews/details.html"
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         rev_id = kwargs['id'] #Look at this thing
#         selected_review = Review.objects.get(pk = rev_id)
#         context["review"] = selected_review
#         return context
    
    