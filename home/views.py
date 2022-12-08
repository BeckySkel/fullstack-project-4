from django.shortcuts import render
from django.views import View, generic
from recipes.models import Recipe


class HomePage(generic.ListView):
    """
    View to display all recipes in the home page
    """
    # code insprired by CI walkthrough project
    model = Recipe
    queryset = Recipe.objects.all().filter(removed=False, private=False)
    template_name = "index.html"
    paginate_by = 9


TAGS = [
    ('Breakfast', 'breakfast'),
    ('Lunch', 'lunch'),
    ('Dinner', 'dinner'),
    ('Dessert', 'dessert'),
    ('Quick and Easy', 'quick-and-easy'),
    ('Low Calorie', 'low-calorie'),
    ('Healthy', 'healthy'),
    ('Vegetarian', 'vegetarian'),
    ('Vegan', 'vegan'),
    ('Low Carb', 'low-carb'),
    ('Gluten Free', 'gluten-free'),
    ('On a Budget', 'on-a-budget'),
    ('Prep Ahead', 'prep-ahead'),
]


class BrowseByTag(View):
    """"""
    def get(self, request, slug, *args, **kwargs):
        for tuple in TAGS:
            if slug in tuple:
                tag = tuple[0]
                
        recipes = Recipe.objects.filter(removed=False, private=False, tags__contains=tag)

        return render(
            request,
            'browse.html',
            {
                'recipes': recipes,
                'tag': tag,
                'slug': slug,
            },
        )