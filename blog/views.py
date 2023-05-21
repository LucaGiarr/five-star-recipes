from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from .models import Recipe


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class StartersList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1, category=0)
    template_name = 'starters.html'


class MainCoursesList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1, category=1)
    template_name = 'maincourses.html'


class DessertsList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1, category=2)
    template_name = 'desserts.html'


class OtherList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1, category=3)
    template_name = 'other.html'
