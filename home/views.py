from django.shortcuts import render
from django.views import View
from django.db.models import Count, Q
from recipes.models import Recipe
from utils.constants import TAGS


class HomePage(View):
    """
    View to make public recipes available as template variables
    to the home page

    new_recipe: queryset, all recipes in order of newest to oldest
    popular_recipes: queryset, all recipes in order of popularity
    """
    def get(self, request, *args, **kwargs):
        new_recipes = Recipe.objects.filter(removed=False, private=False)\
            .order_by('-created_on')

        # Order by count of ManyToMany field from
        # https://stackoverflow.com/questions/28254142/django-order-by-count-of-many-to-many-object
        popular_recipes = Recipe.objects.filter(removed=False, private=False)\
            .annotate(q_count=Count('likes')).order_by('-q_count')

        return render(
                request,
                'index.html',
                {
                    'new_recipes': new_recipes,
                    'popular_recipes': popular_recipes,
                },
            )


class BrowseByTag(View):
    """
    Custom view to display recipes matching the selected tag. Tags are accessed
    via a tuple of tuples called TAGS in utils.constants
    
    recipes: queryset, items from Recipe model whose tag field contains the
    selected tag
    tag: str, the tag name, as it appears to the user
    slug: str, slugified version of the selected tag
    """
    def get(self, request, slug, *args, **kwargs):
        if slug == 'new':
            recipes = Recipe.objects.filter(removed=False, private=False)\
                .order_by('-created_on')
            tag = 'New'
        elif slug == 'popular':
            # Order by count of ManyToMany field from
            # https://stackoverflow.com/questions/28254142/django-order-by-count-of-many-to-many-object
            recipes = Recipe.objects.filter(removed=False, private=False)\
                .annotate(q_count=Count('likes')).order_by('-q_count')
            tag = 'Popular'
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

    searched: str, input retrieved from search bar
    recipes: queryset, items from Recipe model containing the search term
    """
    # Tutorial to retrieve search term available at
    # https://www.youtube.com/watch?v=AGtae4L5BbI
    def post(self, request, *args, **kwargs):
        searched = request.POST['search-bar']
        recipes = Recipe.objects.filter(
            Q(title__icontains=searched) |
            Q(caption__icontains=searched) |
            Q(ingredients__icontains=searched) |
            Q(tags__icontains=searched),
            removed=False,
            private=False
            )

        return render(
            request,
            'search_results.html',
            {'searched': searched, 'recipes': recipes}
            )

    def get(self, request, *args, **kwargs):
        return render(request, 'search_results.html')


def error_404_view(request, exception):
    """
    Custome 404 page

    Tutorial at https://www.geeksforgeeks.org/django-creating-a-404-error-page/
    """
    return render(request, '404.html')


def error_500_view(request):
    """
    Custome 500 page

    Inspired by https://www.geeksforgeeks.org/django-creating-a-404-error-page/
    """
    return render(request, '500.html')