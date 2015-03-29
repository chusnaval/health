from django.db import models


class RecipeType(models.Model):
    name = models.CharField(max_length=50)

    def _str_(self):
        return "%s" % self.name


class NutritionalInformation(models.Model):
    calories = models.IntegerField()
    fat = models.IntegerField()
    saturedFat = models.IntegerField()
    sugar = models.IntegerField()
    salt = models.IntegerField()


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    cooktime = models.IntegerField()
    servings = models.IntegerField()
    type = models.OneToOneField(RecipeType)
    nutritional = models.OneToOneField(NutritionalInformation)

    def _str_(self):
        return "%s" % self.name


from enum import Enum


class UnitType(Enum):
    volume = 1
    mass = 2
    length = 3
    temperature = 4


class Unit(Enum):
    teaspoon = 1
    tablespoon = 2
    cup = 3
    milliliter = 4
    liter = 5
    deciliter = 6
    milligram = 7
    gram = 8
    kilogram = 9
    millimeter = 10
    centimeter = 11
    meter = 12
    celsiusGrade = 13
    unitType = {UnitType.volume: [teaspoon, tablespoon, cup, milliliter, liter, deciliter],
                UnitType.mass: [milligram, gram, kilogram],
                UnitType.length: [milliliter, centimeter, meter],
                UnitType.temperature: [celsiusGrade]}


class Measurement(models.Model):
    amount = models.DecimalField(max_digits=6, decimal_places=2)

    def __init__(self):
        self.unit = Unit()


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    measurement = models.OneToOneField(Measurement, primary_key=False)
    recipe = models.ForeignKey(Recipe)

    def __str__(self):
        return super(self.name)


class RecipeInstruction(models.Model):
    order = models.IntegerField()
    text = models.CharField(max_length=1000)
    recipe = models.ForeignKey(Recipe)

    def __str__(self):
        return super(self.text)


class RecipeTags(models.Model):
    name = models.CharField(max_length=50)
    recipe = models.ForeignKey(Recipe)




