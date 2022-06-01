from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

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


class ArtistCreate(CreateView):
    model = Animal
    fields['name', 'img', 'bio', 'extinct_animal']
