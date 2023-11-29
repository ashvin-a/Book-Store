from django.urls import path
from . import views

urlpatterns = [
    path("",views.ReviewView.as_view()),
    path("thankuu",views.ThankuView.as_view()) #oru '/' mathi ithu mothom 3gkkan😥
]
