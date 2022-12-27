from .models import Recipe, Comment
from django import forms
from utils.constants import TAGS
from profiles.models import Note


class RecipeForm(forms.ModelForm):
    """
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
    # https://openclassrooms.com/en/courses/7107341-intermediate-django/7264795-include-multiple-forms-on-a-page
    commenting = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
          'body': 'Write a comment'
        }
        # https://stackoverflow.com/questions/6536373/how-can-i-set-the-size-of-rows-columns-in-textfield-in-django-models
        widgets = {
          'body': forms.Textarea(attrs={'rows':2, 'cols':15}),
        }


class NoteForm(forms.ModelForm):
    # https://openclassrooms.com/en/courses/7107341-intermediate-django/7264795-include-multiple-forms-on-a-page
    new_note = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = Note
        fields = ('body',)
        labels = {
          'body': 'Write a note'
        }
        # https://stackoverflow.com/questions/6536373/how-can-i-set-the-size-of-rows-columns-in-textfield-in-django-models
        widgets = {
          'body': forms.Textarea(attrs={'rows':2, 'cols':15}),
        }