from django.db import models
from recipe.models import Recipe

class RecipeTags(models.Model):
    name = models.CharField(max_length=50)
    recipe = models.ForeignKey(Recipe)

