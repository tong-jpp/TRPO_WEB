from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'recipe')  # один рецепт можно добавить в избранное только один раз
    
    def __str__(self):
        return f"{self.user.username} - {self.recipe.title}"