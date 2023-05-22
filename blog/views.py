from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .models import Recipe
from .forms import CommentForm


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


class RecipeDetails(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_details.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_details.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
                "comment_form": CommentForm()
            },
        )
