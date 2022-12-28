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
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
import json


class RecipeDetail(View):
    """
    Custom view to display full recipe detail

    recipe: object, object from Recipe model matching the requested slug
    comments: queryset, items from Comment model with matching recipe
    foreign key
    comment_form: form, form for users to add comments to Comment model
    note_form: form, form for users to add comments to Note model
    liked: boolean, True if user has like recipe
    saved: boolean, True if user has saved recipe
    notes: queryset, items from Note model with matching recipe foreign key
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(removed=False)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.recipe_comments.filter(removed=False)
        liked = recipe.likes.filter(id=request.user.id).exists()

        try:
            profile = request.user.profile
            saved = recipe.saved_by.filter(id=request.user.profile.id).exists()
        except AttributeError:
            profile = None
            saved = False

        notes = recipe.notes_for_recipe.filter(profile=profile)

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
        liked = recipe.likes.filter(id=request.user.id).exists()

        try:
            profile = request.user.profile
            saved = recipe.saved_by.filter(id=request.user.profile.id).exists()
        except AttributeError:
            profile = None
            saved = False

        notes = recipe.notes_for_recipe.filter(profile=profile)

        # Code to host multiple forms on single template from
        # https://openclassrooms.com/en/courses/7107341-intermediate-django/7264795-include-multiple-forms-on-a-page
        if 'commenting' in request.POST:
            comment_form = CommentForm(data=request.POST or None)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.commenter = request.user
                comment.recipe = recipe
                comment_form.save()

        # Code to host multiple forms on single template from
        # https://openclassrooms.com/en/courses/7107341-intermediate-django/7264795-include-multiple-forms-on-a-page
        if 'new_note' in request.POST:
            note_form = NoteForm(data=request.POST or None)
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
                'notes': notes,
            },
        )


class AddRecipe(LoginRequiredMixin, View):
    """
    View to host form for users to post new recipe.
    Login required

    recipe_form: form, creates new object in Recipe model once submitted
    """
    def get(self, request, *args, **kwargs):

        return render(
            request,
            'add_recipe.html',
            {'recipe_form': RecipeForm()}
            )

    def post(self, request, *args, **kwargs):
        recipe_form = RecipeForm(request.POST, request.FILES)

        if recipe_form.is_valid():
            recipe_form.instance.author = request.user
            # Idea for holding temporary data to clean
            # https://www.geeksforgeeks.org/multiplechoicefield-django-forms/
            temp = recipe_form.cleaned_data.get('tags')
            recipe = recipe_form.save(commit=False)
            recipe.tags = temp
            recipe_form.save()

            slug = recipe_form.instance.slug

            return redirect(reverse("recipe_detail", kwargs={"slug": slug}))
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


class EditRecipe(LoginRequiredMixin, View):
    """
    View to host form for users to edit their existing recipes.
    Login required

    recipe_form: form, updates instance of recipe in Recipe model
    once submitted
    recipe: object, recipe to edit
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(removed=False)
        recipe = get_object_or_404(queryset, slug=slug)

        recipe_form = RecipeForm(
            instance=recipe,
            initial={'tags': recipe.list_of_tags}
            )

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

        recipe_form = RecipeForm(
            request.POST,
            request.FILES,
            instance=recipe
            )

        if recipe_form.is_valid():
            # Idea for holding temporary data to clean
            # https://www.geeksforgeeks.org/multiplechoicefield-django-forms/
            temp = recipe_form.cleaned_data.get('tags')
            recipe = recipe_form.save(commit=False)
            recipe.updated_on = datetime.now()
            recipe.tags = temp
            updated_recipe = recipe_form.save()

            slug = updated_recipe.slug

            return redirect(reverse("recipe_detail", kwargs={"slug": slug}))
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
                'edit_recipe.html',
                {
                    'recipe_form': RecipeForm(data),
                    'recipe': recipe
                    }
                )


# code from CI Think Blog walkthrough project
class RecipeLike(LoginRequiredMixin, View):
    """
    Toggles like status on submission of like form/button on recipe page.
    Login required
    """
    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


class RecipeSave(LoginRequiredMixin, View):
    """
    Toggles save status on submission of save form/button on recipe page.
    Login required
    """
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


@login_required
def delete_comment(request, comment_id):
    """
    Deletes user's comment from the Comment data model when url called.
    Login required
    """
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.commenter:
        comment.delete()

    # Return to previous page from
    # https://stackoverflow.com/questions/50006147/how-to-return-redirect-to-previous-page-in-django-after-post-request
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def delete_note(request, note_id):
    """
    Deletes user's note from the Note data model when url called.
    Login required
    """
    note = get_object_or_404(Note, id=note_id)
    if request.user.profile == note.profile:
        note.delete()

    # Return to previous page from
    # https://stackoverflow.com/questions/50006147/how-to-return-redirect-to-previous-page-in-django-after-post-request
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def delete_recipe(request, slug):
    """
    Deletes recipe from the Recipe data model when url called.
    Login required
    """
    recipe = get_object_or_404(Recipe, slug=slug)
    if request.user == recipe.author:
        recipe.delete()

    return redirect('/')
