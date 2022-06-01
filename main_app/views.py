from xml.dom.minidom import AttributeList
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse

from .models import Animal

# Create your views here.


class Home(TemplateView):
    template_name = "home.html"


class About(TemplateView):
    template_name = "about.html"


class AnimalList(TemplateView):
    template_name = "animal_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["animals"] = Animal.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["animals"] = Animal.objects.all()
            context["header"] = "Trending Animals"
        return context


class AnimalCreate(CreateView):
    model = Animal
    fields = ['name', 'img', 'bio', 'extinct_animal']
    template_name = "animal_create.html"
    success_url = "/animals/"

    def get_success_url(self):
        return reverse('animal_detail', kwargs={'pk': self.object.pk})


class AnimalDetail(DetailView):
    model = Animal
    template_name = "animal_detail.html"


class AnimalUpdate(UpdateView):
    model = Animal
    fields = ['name', 'img', 'bio', 'extinct_animal']
    template_name = "animal_update.html"
    success_url = "/animals/"

    def get_success_url(self):
        return reverse('animal_detail', kwargs={'pk': self.object.pk})


class AnimalDelete(DeleteView):
    model = Animal
    template_name = "animal_delete_confirmation.html"
    success_url = "/animals/"
