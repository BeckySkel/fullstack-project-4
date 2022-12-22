from .models import Profile
from django import forms
from utils.utils import TAGS
from profiles.models import Note

class ProfileForm(forms.ModelForm):
    """"""

    class Meta:
        model = Profile
        fields = (
            'first_name',
            'last_name',
            'profile_image',
            'bio',
        )