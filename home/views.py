from django.shortcuts import render
from django.views import View, generic
from recipes.models import Recipe
from django.db.models import Q


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


class SearchResults(View):
    """"""
    # https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/dc049b343a9b474f8d75822c5fda1582/22da66e7007d4b5a9bd53901c84034e8/
    def post(self, request, *args, **kwargs):
        search = request.POST['search-bar']
        recipes = Recipe.objects.filter(Q(title__icontains=search) | Q(caption__icontains=search) | Q(ingredients__icontains=search) | Q(tags__icontains=search))
        all_recipes = Recipe.objects.all()
        return render(request, 'search_results.html', {'search': search, 'recipes': recipes })

    def get(self, request, *args, **kwargs):
        return render(request, 'search_results.html')
