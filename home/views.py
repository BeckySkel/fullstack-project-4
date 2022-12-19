from django.shortcuts import render
from django.views import View, generic
from recipes.models import Recipe
from django.db.models import Count
from django.db.models import Q
from utils.utils import TAGS


class HomePage(generic.ListView):
    """
    List view to make public recipes available as
    'recipe_list' template variable to the home page
    """
    # code insprired by CI walkthrough project
    model = Recipe
    queryset = Recipe.objects.all().filter(removed=False, private=False)
    template_name = "index.html"


class BrowseByTag(View):
    """
    Custom view to display recipes matching the selected tag. Tags are access
    via a tuple of tuples called TAGS
    
    recipes: queryset, items from Recipe model whose tag field contains the
    selected tag
    tag: str, the tag name, as it appears to the user
    slug: str, slugified version of the selected tag
    """
    def get(self, request, slug, *args, **kwargs):
        if slug == 'new':
            recipes = Recipe.objects.filter(removed=False, private=False).order_by('-created_on')
            tag = 'new'
        elif slug == 'popular':
            # https://stackoverflow.com/questions/28254142/django-order-by-count-of-many-to-many-object
            recipes = Recipe.objects.filter(removed=False, private=False).annotate(q_count=Count('likes')).order_by('-q_count')
            tag = 'popular'
        else:
            for tuple in TAGS:
                if slug in tuple:
                    tag = tuple[0]
                    
            recipes = Recipe.objects.filter(
                removed=False,
                private=False,
                tags__contains=tag
                )

        return render(
            request,
            'browse.html',
            {
                'recipes': recipes,
                'tag': tag,
                'slug': slug,
            },
        )


class SearchResults(View):
    """
    Custom view for displaying search results. Checks if the inputted string
    appears in the title, caption, ingredients list or tags of a recipe.

    search: str, input retrieved from search bar
    recipes: queryset, items from Recipe model containing the search term
    """
    # Tutorial to retrieve search term available at
    # https://www.youtube.com/watch?v=AGtae4L5BbI
    def post(self, request, *args, **kwargs):
        search = request.POST['search-bar']
        recipes = Recipe.objects.filter(
            Q(title__icontains=search) |
            Q(caption__icontains=search) |
            Q(ingredients__icontains=search) |
            Q(tags__icontains=search),
            removed=False,
            private=False
            )

        return render(
            request,
            'search_results.html',
            {'search': search, 'recipes': recipes}
            )

    def get(self, request, *args, **kwargs):
        return render(request, 'search_results.html')

