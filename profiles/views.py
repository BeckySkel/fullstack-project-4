from recipes.models import Recipe
from profiles.models import Profile
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import View
from django.db.models import Q


class ProfilePage(View):
    """"""
    def get(self, request, profile_id, *args, **kwargs):
        profile = get_object_or_404(Profile, id=profile_id)
        recipes = Recipe.objects.filter(removed=False)
        saved_recipes = recipes.filter(saved_by=profile_id)
        posted_recipes = recipes.filter(author=profile.user)

        return render(
            request,
            'profile.html',
            {
                'recipes': recipes,
                'saved_recipes': saved_recipes,
                'posted_recipes': posted_recipes,
                'profile': profile,
            },
        )  
