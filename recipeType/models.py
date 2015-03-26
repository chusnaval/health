from django.db import models


class RecipeType(models.Model):
    name = models.CharField(max_length=50)

    def _str_(self):
        return "%s" % (self.name)