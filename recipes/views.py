from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic.detail import DetailView
from .models import Recipe
from .forms import RecipeForm
from django.contrib import messages
from multiurl import ContinueResolving


class RecipeDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(removed=False)
        recipe = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe
            },
        )


class AddRecipe(View):
    
    def get(self, request, *args, **kwargs):

        return render(
            request,
            'add_recipe.html',
            {'recipe_form': RecipeForm()}
            )

    def post(self, request, *args, **kwargs):

        recipe_form = RecipeForm(data=request.POST)
        
        if recipe_form.is_valid():
            recipe_form.instance.author = request.user
            recipe = recipe_form.save()

            slug = recipe_form.instance.slug
            
            return redirect(f'/recipes/{slug}')
        else:
            data = {
                'title': recipe_form.instance.title,
                'caption': recipe_form.instance.caption,
                'image': recipe_form.instance.image,
                'ingredients': recipe_form.instance.ingredients,
                'steps': recipe_form.instance.steps,
                }
            # https://docs.djangoproject.com/en/dev/ref/forms/api/#dynamic-initial-values
            # https://www.reddit.com/r/django/comments/4oie1d/how_to_automatically_prepopulate_data_in_forms/
            return render(
                request,
                'add_recipe.html',
                {'recipe_form': RecipeForm(data)}
                )


