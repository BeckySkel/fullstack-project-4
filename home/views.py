from django.shortcuts import render
from django.views import View, generic
from recipes.models import Recipe


class HomePage(generic.ListView):
    """
    View to display all recipes in the home page
    """

    model = Recipe
    queryset = Recipe.objects.all().filter(removed=False)
    template_name = "index.html"
    paginate_by = 9