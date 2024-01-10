from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import DetailView
from django.http import HttpResponseRedirect
from .models import Recipe, UserProfile
from .forms import RecipeForm, CommentForm
from django.urls import reverse_lazy


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

    def get(self, request, slug):
        queryset = Recipe.objects.all()
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')

        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        isFavourite = False
        if recipe.favourites.filter(id=self.request.user.id).exists():
            isFavourite = True

        return render(
            request,
            "recipe_details.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "isFavourite": isFavourite,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')

        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        isFavourite = False
        if recipe.favourites.filter(id=self.request.user.id).exists():
            isFavourite = True

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
                "liked": liked,
                "isFavourite": isFavourite,
                "comment_form": CommentForm()
            },
        )


class PersonalRecipesList(generic.ListView):
    model = Recipe
    template_name = 'personal_recipes.html'

    def get_queryset(self):
        return Recipe.objects.filter(author=self.request.user)


class RecipeCreateView(generic.CreateView):
    form_class = RecipeForm
    template_name = 'recipe_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)

        # Set a session variable to indicate that the recipe was just created
        if form.instance.status == 0:
            self.request.session['recipe_message'] = 'Draft created successfully.'
        else:
            self.request.session['recipe_message'] = 'Recipe created successfully.'

        return response


class RecipeEditView(generic.UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'edit_recipe.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)

        # Set a session variable to indicate that the recipe was just edited
        self.request.session['recipe_message'] = 'Recipe updated successfully.'

        return response


class RecipeDeleteView(generic.DeleteView):
    model = Recipe
    template_name = 'delete_recipe.html'
    success_url = reverse_lazy('personal_recipes')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)

        # Set a session variable to indicate that the recipe was just deleted
        self.request.session['recipe_deleted'] = 'Recipe deleted successfully.'

        return response


class RecipeLike(View):

    def post(self, request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.likes.filter(id=self.request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_details', args=[slug]))


class RecipeFavourite(View):

    def post(self, request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.favourites.filter(id=self.request.user.id).exists():
            recipe.favourites.remove(request.user)
        else:
            recipe.favourites.add(request.user)

        return HttpResponseRedirect(reverse('recipe_details', args=[slug]))


class ShowProfilePage(DetailView):
    model = UserProfile
    template_name = 'account/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePage, self).get_context_data(
            *args, **kwargs)

        page_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])

        context["page_user"] = page_user
        return context


def favourite_list(request):
    fav_list = Recipe.objects.filter(favourites=request.user)
    return render(request, 'favourites.html', {'fav_list': fav_list})
