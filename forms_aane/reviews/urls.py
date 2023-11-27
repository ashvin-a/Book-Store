from django.urls import path
from . import views

urlpatterns = [
    path("",views.reviews),
    path("thankuu",views.thanku) #oru '/' mathi ithu mothom 3gkkan😥
]
