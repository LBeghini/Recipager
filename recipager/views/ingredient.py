from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
from django.http import HttpResponse

from ..models import Ingredient
from django.http import JsonResponse


def index(request):
    ingredients_list = Ingredient.objects.all()
    context = {'ingredients_list': ingredients_list}
    return render(request, 'recipager/ingredient/index.html', context)


def detail(request, ingredient_id):
    ingredient = get_object_or_404(Ingredient, pk=ingredient_id)
    return render(request, 'recipager/ingredient/detail.html', {'ingredient': ingredient})


def add(request):
    if request.method == "POST":
        ingredient = Ingredient(
            name=request.POST['name'], cost=request.POST['cost'], quantity=request.POST['quantity'], unit=request.POST['unit'])
        ingredient.save()
        ingredient.article_number = str(ingredient.id).rjust(13, '0')
        ingredient.save()
        return redirect('recipager:ingredient')
    else:
        return render(request, 'recipager/ingredient/form.html')


def edit(request, ingredient_id):
    ingredient = Ingredient.objects.get(pk=ingredient_id)
    if request.method == "POST":
        ingredient.name = request.POST['name']
        ingredient.cost = request.POST['cost']
        ingredient.quantity = request.POST['quantity']
        ingredient.unit = request.POST['unit']
        ingredient.save()
        return redirect('recipager:ingredient')
    else:
        return render(request, 'recipager/ingredient/form.html', {'ingredient': ingredient})


def all(request):
    print('here')
    ingredients = Ingredient.objects.all()
    ingredient_list = {}
    for ingredient in ingredients:
        ingredient_list[f'{ingredient.name} - {ingredient.article_number}'] = None

    return JsonResponse(ingredient_list)
