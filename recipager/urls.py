from django.urls import path

from .views import recipe, ingredient, index

app_name = 'recipager'
urlpatterns = [
    path('', index.index, name='index'),
    path('recipe', recipe.index, name='recipe'),
    path('recipe/add', recipe.add, name='recipe_add'),
    path('recipe/<int:recipe_id>/', recipe.detail, name='recipe_detail'),
    path('recipe/<int:recipe_id>/edit/', recipe.edit, name='recipe_edit'),
    path('ingredient', ingredient.index, name='ingredient'),
    path('ingredient/add', ingredient.add, name='ingredient_add'),
    path('ingredient/<int:ingredient_id>/edit', ingredient.edit, name='ingredient_edit'),
    path('ingredient/all', ingredient.all, name='ingredient_all'),
]
