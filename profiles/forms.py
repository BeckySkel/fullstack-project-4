from .models import Profile
from django import forms
from utils.constants import TAGS
from profiles.models import Note


class ProfileForm(forms.ModelForm):
    """
    Profile editor, called immediately after user registers and/or any time
    user would like to update
    """

    class Meta:
        model = Profile
        fields = (
            'first_name',
            'last_name',
            'profile_image',
            'bio',
        )
