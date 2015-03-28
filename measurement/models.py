from django.db import models
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
    unitType = {UnitType.volume: [teaspoon, tablespoon,cup,milliliter,liter,deciliter],
                UnitType.mass: [milligram, gram, kilogram],
                UnitType.length: [milliliter, centimeter, meter],
                UnitType.temperature: [celsiusGrade]}


class Measurement(models.Model):
    amount = models.DecimalField(max_digits=6, decimal_places=2)

    def __init__(self):
        self.unit = Unit()