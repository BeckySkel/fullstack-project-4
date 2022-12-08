from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import View
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from .models import Recipe, Comment
from .forms import RecipeForm, CommentForm
from django.contrib import messages
from multiurl import ContinueResolving


class RecipeDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(removed=False)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.recipe_comments.filter(removed=False)
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'recipe_detail.html',
            {
                'recipe': recipe,
                'comments': comments,
                'comment_form': CommentForm(),
                'liked': liked
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(removed=False)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.recipe_comments.filter(removed=False)
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True
        comment_form = CommentForm(data=request.POST or None)
        
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)

            comment.commenter = request.user
            comment.recipe = recipe
            comment_form.save()
            print('saved :)')
        else:
            print('failed :(')

        return render(
            request,
            'recipe_detail.html',
            {
                'recipe': recipe,
                'comments': comments,
                'comment_form': CommentForm(),
                'liked': liked
            },
        )


# code from CI Think Blog walkthrough project
class RecipeLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


def delete_comment(request, comment_id):
    
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('home')


class AddRecipe(View):
    
    def get(self, request, *args, **kwargs):

        return render(
            request,
            'add_recipe.html',
            {'recipe_form': RecipeForm()}
            )

    def post(self, request, *args, **kwargs):

        recipe_form = RecipeForm(data=request.POST or None)
        
        if recipe_form.is_valid():
            recipe_form.instance.author = request.user
            # https://www.geeksforgeeks.org/multiplechoicefield-django-forms/
            temp = recipe_form.cleaned_data.get('tags')
            recipe = recipe_form.save(commit=False)
            recipe.tags = temp
            recipe_form.save()

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


class EditRecipe(View):
    
    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(removed=False)
        recipe = get_object_or_404(queryset, slug=slug)

        recipe_form = RecipeForm(instance=recipe)
        
        return render(
            request,
            'edit_recipe.html',
            {
                'recipe_form': recipe_form,
                'recipe': recipe
            })

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(removed=False)
        recipe = get_object_or_404(queryset, slug=slug)

        recipe_form = RecipeForm(data=request.POST or None, instance=recipe)
        
        if recipe_form.is_valid():
            # https://www.geeksforgeeks.org/multiplechoicefield-django-forms/
            temp = recipe_form.cleaned_data.get('tags')
            recipe = recipe_form.save(commit=False)
            recipe.tags = temp
            updated_recipe = recipe_form.save()
            slug = updated_recipe.slug
            
            return redirect(f'/recipes/{slug}')
        else:
            data = {
                'title': recipe_form.instance.title,
                'caption': recipe_form.instance.caption,
                'image': recipe_form.instance.image,
                'ingredients': recipe_form.instance.ingredients,
                'steps': recipe_form.instance.steps,
                'private': recipe_form.instance.private,
                'tags': recipe_form.instance.tags,
                }
            # https://docs.djangoproject.com/en/dev/ref/forms/api/#dynamic-initial-values
            # https://www.reddit.com/r/django/comments/4oie1d/how_to_automatically_prepopulate_data_in_forms/
            return render(
                request,
                'add_recipe.html',
                {'recipe_form': RecipeForm(data)}
                )

