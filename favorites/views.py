from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Favorite
from recipes.models import Recipe

@login_required
def favorite_recipes(request):
    favorites = Favorite.objects.filter(user=request.user).select_related('recipe')
    return render(request, 'favorites/favorite_recipes.html', {'favorites': favorites})

@login_required
def add_to_favorites(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    favorite, created = Favorite.objects.get_or_create(
        user=request.user, 
        recipe=recipe
    )
    if created:
        messages.success(request, f'Рецепт "{recipe.title}" добавлен в избранное')
    else:
        messages.info(request, f'Рецепт "{recipe.title}" уже в избранном')
    
    return redirect('recipe_detail', recipe_id=recipe_id)

@login_required
def remove_from_favorites(request, recipe_id):
    favorite = get_object_or_404(Favorite, user=request.user, recipe_id=recipe_id)
    recipe_title = favorite.recipe.title
    favorite.delete()
    messages.success(request, f'Рецепт "{recipe_title}" удален из избранного')
    
    return redirect('favorite_recipes')