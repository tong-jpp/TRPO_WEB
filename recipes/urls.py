from django.urls import path
from . import views
from django.shortcuts import render

def home(request):
    return render(request, 'recipes/home.html')
urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.recipe_search, name='recipe_search'),
    path('recipes/', views.all_recipes, name='all_recipes'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
]