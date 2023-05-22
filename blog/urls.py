from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('starters', views.StartersList.as_view(), name='starters'),
    path('maincourses', views.MainCoursesList.as_view(), name='main_courses'),
    path('desserts', views.DessertsList.as_view(), name='desserts'),
    path('other', views.OtherList.as_view(), name='other'),
    path('<slug:slug>/', views.RecipeDetails.as_view(), name='recipe_details'),
]