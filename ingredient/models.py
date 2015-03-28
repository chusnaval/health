from django.db import models
from measurement.models import Measurement
from recipe.models import Recipe





class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    measurement = models.OneToOneField(Measurement, primary_key=False)
    recipe = models.ForeignKey(Recipe)
