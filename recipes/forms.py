from .models import Recipe, Comment
from django import forms


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            'title',
            'caption',
            'image',
            'ingredients',
            'steps',
            'private'
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
          'body': forms.Textarea(attrs={'rows':2, 'cols':15}),
        }