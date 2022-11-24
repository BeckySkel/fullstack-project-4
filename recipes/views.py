from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Recipe


class RecipeDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(removed=False)
        recipe = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            'recipe_detail.html',
            {
                'recipe': recipe
            }
        )