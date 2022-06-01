from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('animals/', views.AnimalList.as_view(), name="animal_list"),
    path('animals/new', views.AnimalCreate.as_view(), name="animal_create"),
    path('animals/<int:pk>/', views.AnimalDetail.as_view(), name="animal_detail"),
    path('animals/<int:pk>/update',
         views.AnimalUpdate.as_view(), name="animal_update"),
    path('animals/<int:pk>/delete',
         views.AnimalDelete.as_view(), name="animal_delete")
]
