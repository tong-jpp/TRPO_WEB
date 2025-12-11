from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Recipe, Ingredient
from .forms import IngredientSearchForm
from favorites.models import Favorite
from django.shortcuts import render
from django.contrib import messages
from django.http import Http404
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from .models import Ingredient

from django.db.models import Count

def home(request):
    return render(request, 'recipes/home.html')

def recipe_search(request):
    if request.method == 'POST':
        form = IngredientSearchForm(request.POST)
        if form.is_valid():
            user_ingredients = [x.strip().lower() for x in form.cleaned_data['ingredients'].split(',')]      
            recipes = Recipe.objects.all()
            matching_recipes = []
            
            for recipe in recipes:
                recipe_ingredients = [ing.name.lower() for ing in recipe.ingredients.all()]
                
                base_ingredients = []
                for ing in recipe_ingredients:
                    if "(" in ing or ")" in ing:
                        base_ingredients.append(ing[:ing.find("(")].strip())
                    else:
                        base_ingredients.append(ing.strip())
                
                matches = 0
                for user_ing in user_ingredients:
                    if "(" in user_ing or ")" in user_ing:
                        if user_ing in recipe_ingredients:
                            matches += 1
                    else:
                        if user_ing in base_ingredients:
                            matches += 1
                
                if matches > 0:
                    matching_recipes.append({
                        'recipe': recipe,
                        'match_count': matches,
                        'match_percentage': (matches / len(recipe_ingredients)) * 100
                    })
            
            matching_recipes.sort(key=lambda x: x['match_percentage'], reverse=True)
            
            return render(request, 'recipes/search_results.html', {
                'recipes_data': matching_recipes,
                'search_ingredients': user_ingredients,
                'form': form
            })
    else:
        form = IngredientSearchForm()
    
    return render(request, 'recipes/search.html', {'form': form})

def all_recipes(request):
    recipes = Recipe.objects.all()

    time_min = request.GET.get('time_min')
    time_max = request.GET.get('time_max')
    if time_min:
        recipes = recipes.filter(cooking_time__gte=int(time_min))
    if time_max:
        recipes = recipes.filter(cooking_time__lte=int(time_max))

    ingredients_count = request.GET.get('ingredients_count')
    if ingredients_count:
        recipes = recipes.annotate(num_ing=Count('ingredients')).filter(num_ing__gte=int(ingredients_count))

    order = request.GET.get('order')
    if order == 'asc':
        recipes = recipes.order_by('title')
    elif order == 'desc':
        recipes = recipes.order_by('-title')
    else:
        recipes = recipes.order_by('-created_at')

    return render(request, 'recipes/all_recipes.html', {'recipes': recipes})


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    is_favorite = False
    if request.user.is_authenticated:
        is_favorite = Favorite.objects.filter(user=request.user, recipe=recipe).exists()
    
    return render(request, 'recipes/recipe_detail.html', {
        'recipe': recipe,
        'is_favorite': is_favorite
    })


def ingredient_autocomplete(request):
    query = request.GET.get('term', '').lower()
    if query:
        ingredients = Ingredient.objects.all()
        suggestions = [
            ing.name for ing in ingredients
            if query in ing.name.lower() 
        ][:5]
        return JsonResponse(suggestions, safe=False)
    return JsonResponse([], safe=False)

def favorites(request):
    return render(request, "favorite_recipes.html")

def remove_favorite(request, recipe_id):
    if request.user.is_authenticated:
        try:
            favorite = Favorite.objects.get(user=request.user, recipe_id=recipe_id)
            favorite.delete()
            messages.success(request, "Рецепт удален из избранного.")
        except Favorite.DoesNotExist:
            messages.info(request, "Этот рецепт уже не в избранном.")
        
        return redirect('favorite_recipes')
    else:
        return redirect('login')