from django.db import models
from recipe.models import Recipe


class RecipeInstruction(models.Model):
    order = models.IntegerField()
    text = models.CharField(max_length=1000)
    recipe = models.ForeignKey(Recipe)

    def __str__(self):
        return super(self.text)