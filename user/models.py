from django.db import models

# Create your models here.
class User(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=30)

    def _str_(self):
        return "%s" % (self.login)
