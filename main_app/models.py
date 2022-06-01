from django.db import models

# Create your models here.


class Animal(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    bio = models.TextField(max_length=500)
    extinct_animal = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Group(models.Model):
    name = models.CharField(max_length=100)
    animal = models.ForeignKey(
        Animal, on_delete=models.CASCADE, related_name="groups")

    def __str__(self):
        return self.name


class Location(models.Model):
    title = models.CharField(max_length=150)
    animals = models.ManyToManyField(Animal)

    def __str__(self):
        return self.title
