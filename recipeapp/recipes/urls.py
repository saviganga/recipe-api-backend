from django.urls import path, include
from .views import RecipeView

urlpatterns = [
    path('', RecipeView.as_view()),
]