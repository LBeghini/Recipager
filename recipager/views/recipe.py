from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
from django.http import HttpResponse
from ..models import Item, Recipe


def index(request):
    recipes_list = Recipe.objects.all()
    context = {'recipes_list': recipes_list}
    return render(request, 'recipager/recipe/index.html', context)


def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    ingredients = recipe.ingredients.all()
    ingredient_list = []
    for ingredient in ingredients:
        ingredient_list.append({
            "name": ingredient.name,
            "amount": ingredient.item_set.get(recipe=recipe).amount,
            "cost": ingredient.cost,
            "unit": ingredient.unit,
            "quantity": ingredient.quantity
        })

    recipe_cost = 0
    for ingredient in ingredient_list:
        recipe_cost += (ingredient['amount'] *
                        ingredient['cost']) / ingredient['quantity']

    recipe_cost = round(recipe_cost, 2)

    return render(request, 'recipager/recipe/detail.html', {'recipe': recipe, 'ingredients': ingredient_list, 'total': recipe_cost})


def add(request):
    if request.method == "POST":
        recipe = Recipe()
        return redirect('recipager:recipes_aall')
    else:
        return render(request, 'recipager/recipe/form.html')


def edit(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return HttpResponse("You're voting on recipe %s." % recipe_id)

# def form(request, recipe_id):
#     recipe = get_object_or_404(Recipe, pk=recipe_id)
#     return render(request, 'recipager/recipe/form.html', {'recipe': recipe})
