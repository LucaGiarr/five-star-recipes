from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('starters/', views.StartersList.as_view(), name='starters'),
]
