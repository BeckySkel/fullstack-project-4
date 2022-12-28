from .models import Recipe, Comment
from django import forms
from utils.constants import TAGS
from profiles.models import Note


class RecipeForm(forms.ModelForm):
    """
    Recipe creator/editor form
    """
    tags = forms.MultipleChoiceField(
      choices=TAGS,
      widget=forms.CheckboxSelectMultiple()
      )

    class Meta:
        model = Recipe
        fields = (
            'title',
            'caption',
            'image',
            'ingredients',
            'steps',
            'private',
        )


class CommentForm(forms.ModelForm):
    """
    Form to post public comments to recipes
    """
    # Code for multiple forms in one template from
    # https://openclassrooms.com/en/courses/7107341-intermediate-django/7264795-include-multiple-forms-on-a-page
    commenting = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
          'body': 'Write a comment'
        }
        # Formatting textarea widget from
        # https://stackoverflow.com/questions/6536373/how-can-i-set-the-size-of-rows-columns-in-textfield-in-django-models
        widgets = {
          'body': forms.Textarea(attrs={'rows': 2, 'cols': 15}),
        }


class NoteForm(forms.ModelForm):
    """
    Form to add private notes to recipes
    """
    # Code for multiple forms in one template from
    # https://openclassrooms.com/en/courses/7107341-intermediate-django/7264795-include-multiple-forms-on-a-page
    new_note = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = Note
        fields = ('body',)
        labels = {
          'body': 'Write a note'
        }
        # Formatting textarea widget from
        # https://stackoverflow.com/questions/6536373/how-can-i-set-the-size-of-rows-columns-in-textfield-in-django-models
        widgets = {
          'body': forms.Textarea(attrs={'rows': 2, 'cols': 15}),
        }