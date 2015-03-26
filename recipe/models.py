from django.db import models
from recipeType.models import RecipeType


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    cooktime = models.IntegerField()
    type = models.OneToOneField(RecipeType, primary_key=False)

    def _str_(self):
        return "%s" % self.name
