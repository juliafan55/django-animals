from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('animals/', views.AnimalList.as_view(), name="animal_list"),
    path('animals/new', views.AnimalCreate.as_view(), name="animal_create"),
]
