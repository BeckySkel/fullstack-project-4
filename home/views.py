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


class BrowseByTag(View):
    """"""
    def get(self, request, tag, *args, **kwargs):
        recipes = Recipe.objects.filter(removed=False, private=False, tags__contains=tag)

        return render(
            request,
            'browse.html',
            {
                'recipes': recipes,
                'tag': tag
            },
        )