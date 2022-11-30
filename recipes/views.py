from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Recipe
from .forms import RecipeForm
from django.contrib import messages


class AddRecipe(View):
    
    def get(self, request, *args, **kwargs):

        return render(request, 'add_recipe.html', {'recipe_form': RecipeForm()})


    def post(self, request, *args, **kwargs):

        recipe_form = RecipeForm(data=request.POST)
        
        if recipe_form.is_valid():
            recipe_form.instance.author = request.user
            recipe_form.save()
            return render(request, 'add_recipe.html', {'recipe_form': RecipeForm()})
        else:
            # messages.error(request, 'Invalid form response')
            data = {
                'title': recipe_form.instance.title,
                'caption': recipe_form.instance.caption,
                'image': recipe_form.instance.image,
                'ingredients': recipe_form.instance.ingredients,
                'steps': recipe_form.instance.steps,
                }
            recipe_form = RecipeForm()
            return render(request, 'add_recipe.html', {'recipe_form': RecipeForm(data)})


class RecipeDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.all().filter(removed=False)
        recipe = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            'recipe_detail.html',
            {
                'recipe': recipe
            }
        )



