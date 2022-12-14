from .models import Recipe, Comment
from django import forms
from utils.utils import TAGS
from profiles.models import Note

class RecipeForm(forms.ModelForm):
    tags = forms.MultipleChoiceField(choices=TAGS, widget=forms.CheckboxSelectMultiple())

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
    class Meta:
        model = Comment
        fields = ('body',)
        # https://stackoverflow.com/questions/6536373/how-can-i-set-the-size-of-rows-columns-in-textfield-in-django-models
        widgets = {
          'body': forms.Textarea(attrs={'rows':2, 'cols':15}),
        }


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('body',)
        # https://stackoverflow.com/questions/6536373/how-can-i-set-the-size-of-rows-columns-in-textfield-in-django-models
        widgets = {
          'body': forms.Textarea(attrs={'rows':2, 'cols':15}),
        }