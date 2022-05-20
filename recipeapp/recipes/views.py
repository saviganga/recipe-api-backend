from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics
from rest_framework.utils import serializer_helpers
from .serializers import RecipeSerializer
from .models import Recipe
# Create your views here.

class RecipeView(generics.ListCreateAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
