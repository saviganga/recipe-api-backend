from django.db import models

# Create your models here.
class Recipe(models.Model):

    name = models.CharField(max_length=50)
    ingredients = models.TextField(blank=True, null=True)