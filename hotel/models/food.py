from django.db import models


class Recipe(models.Model):
    menu_name = models.CharField(max_length=255)
    portion_size = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Stock(models.Model):
    INGREDIENT_TYPES = [
        ('kg', 'Kilogram'),
        ('g', 'Gram'),
        ('l', 'Liter'),
        ('ml', 'Milliliter'),
    ]

    ingredient_name = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=2, choices=INGREDIENT_TYPES)


class Ingredient(models.Model):
    MEASURE_TYPES = [
        ('kg', 'Kilogram'),
        ('g', 'Gram'),
        ('l', 'Liter'),
        ('ml', 'Milliliter'),
    ]
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    ingredients_measure = models.DecimalField(max_digits=10, decimal_places=2)
    measure_type = models.CharField(max_length=2, choices=MEASURE_TYPES)


class MealList(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    quantity_ordered = models.IntegerField()
