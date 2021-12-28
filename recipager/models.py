from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Ingredient(models.Model):
    
    class UnitChoices(models.TextChoices):
        GRAMS = 'gr', _('grams')
        KILOGRAMS = 'kg', _('kilograms')
        CENTILITER = 'cl', _('centiliter')
        LITER = 'l', _('liter')
        
    name = models.CharField(max_length=200)
    # emoji
    article_number = models.CharField(max_length=13)
    cost = models.DecimalField(max_digits = 5, decimal_places = 2, default=0.0)
    quantity = models.DecimalField(max_digits = 5, decimal_places = 2, default=0.0)
    unit = models.CharField(max_length=2, choices=UnitChoices.choices, default=UnitChoices.GRAMS)

    def is_standard_unit(self):
        return self.unit in (self.UnitChoices.KILOGRAMS, self.UnitChoices.LITER)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(Ingredient, through='Item')

    def __str__(self):
        return self.name

class Item(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits = 5, decimal_places = 2, default=0.0)

    def __str__(self):
        return self.ingredient.name
