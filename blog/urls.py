from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('starters', views.StartersList.as_view(), name='starters'),
    path('maincourses', views.MainCoursesList.as_view(), name='main_courses'),
    path('desserts', views.DessertsList.as_view(), name='desserts'),
    path('other', views.OtherList.as_view(), name='other'),
    path('<int:pk>/profile/',
         views.ShowProfilePage.as_view(), name='user_profile'),
    path('personalrecipes', views.PersonalRecipesList.as_view(),
         name='personal_recipes'),
    path('createrecipe', views.RecipeCreateView.as_view(), name='create_recipe'),
    path('<slug:slug>/edit/',
         views.RecipeEditView.as_view(), name='edit_recipe'),
    path('<slug:slug>/delete/',
         views.RecipeDeleteView.as_view(), name='delete_recipe'),
    path('<slug:slug>/', views.RecipeDetails.as_view(), name='recipe_details'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),
    path('favourite/<slug:slug>',
         views.RecipeFavourite.as_view(), name='recipe_favourite'),
    path('profile/favourites/', views.favourite_list, name='favourite_list'),
]
