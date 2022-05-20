from django.db.models import fields
from .models import Recipe
from rest_framework import serializers

class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = '__all__'