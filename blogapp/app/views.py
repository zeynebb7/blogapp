from django.shortcuts import render
from .models import Recipe, Category

def index(request):
    categories = Category.objects.all()
    recipes = Recipe.objects.all()
    return render(request, "app/index.html", {"categories": categories, "recipes": recipes})