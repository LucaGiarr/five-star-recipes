from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from .models import Recipe


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    # paginate_by = 3
