from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Recipe, Ingredient
from .forms import IngredientSearchForm
from favorites.models import Favorite
from django.shortcuts import render

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

                matches = sum(1 for user_ing in user_ingredients 
                            if any(user_ing in recipe_ing for recipe_ing in recipe_ingredients))
                
                if matches > 0:
                    matching_recipes.append({
                        'recipe': recipe,
                        'match_count': matches,
                        'match_percentage': (matches / len(recipe_ingredients)) * 100
                    })
            
            # Сортировка по проценту совпадений
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
    recipes = Recipe.objects.all().order_by('-created_at')
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