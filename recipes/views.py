from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import View
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from .models import Recipe, Comment
from .forms import RecipeForm, CommentForm, NoteForm
from django.contrib import messages
from multiurl import ContinueResolving
from profiles.models import Note
from datetime import datetime


class RecipeDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(removed=False)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.recipe_comments.filter(removed=False)
        try:
            profile = request.user.profile
            if recipe.saved_by.filter(id=profile.id).exists():
                saved = True
        except AttributeError:
            profile = None
        
        notes = recipe.notes_for_recipe.filter(profile=profile)
                    
        liked = recipe.likes.filter(id=self.request.user.id).exists()
        saved = recipe.saved_by.filter(id=self.request.user.profile.id).exists()
        

        return render(
            request,
            'recipe_detail.html',
            {
                'recipe': recipe,
                'comments': comments,
                'comment_form': CommentForm(),
                'note_form': NoteForm(),
                'liked': liked,
                'saved': saved,
                'notes': notes,
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(removed=False)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.recipe_comments.filter(removed=False)
        notes = recipe.notes_for_recipe.filter(profile=request.user.profile)
        liked = recipe.likes.filter(id=self.request.user.id).exists()
        saved = recipe.saved_by.filter(id=self.request.user.profile.id).exists()
        print(saved)
        comment_form = CommentForm(data=request.POST or None)
        note_form = NoteForm(data=request.POST or None)
        
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)

            comment.commenter = request.user
            comment.recipe = recipe
            comment_form.save()
        
        if note_form.is_valid():
            note = note_form.save(commit=False)

            note.profile = request.user.profile
            note.recipe = recipe
            note_form.save()

        return render(
            request,
            'recipe_detail.html',
            {
                'recipe': recipe,
                'comments': comments,
                'comment_form': CommentForm(),
                'note_form': NoteForm(),
                'liked': liked,
                'saved': saved,
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


class RecipeSave(View):

    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)
        profile = request.user.profile
        if recipe.saved_by.filter(id=request.user.profile.id).exists():
            recipe.saved_by.remove(request.user.profile.id)
            print('unsaved')
        else:
            recipe.saved_by.add(request.user.profile.id)
            print('saved')

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.commenter:
        comment.delete()
    # https://stackoverflow.com/questions/50006147/how-to-return-redirect-to-previous-page-in-django-after-post-request
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.user == note.profile:
        note.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete_recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    if request.user == recipe.author:
        recipe.delete()
    return render(request, 'home')


class AddRecipe(View):
    """"""
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
            
            redirect(reverse("recipe_detail", kwargs={"slug": slug}))
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
            recipe.updated_on = datetime.now()
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

