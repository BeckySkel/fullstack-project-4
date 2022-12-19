from recipes.models import Recipe
from profiles.models import Profile
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import View
from django.db.models import Q
from .forms import DashboardViewForm


class ProfilePage(View):
    """"""
    def get(self, request, profile, *args, **kwargs):
        get_user = User.objects.get(username=profile)

        recipes = Recipe.objects.filter(removed=False)
        saved_recipes = recipes.filter(saved_by=get_user.profile)
        posted_recipes = recipes.filter(author=get_user)

        return render(
            request,
            'profile.html',
            {
                'recipes': recipes,
                'saved_recipes': saved_recipes,
                'posted_recipes': posted_recipes,
                'profile': get_user
            },
        )  
