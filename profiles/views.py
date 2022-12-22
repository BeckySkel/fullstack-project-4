from recipes.models import Recipe
from .forms import ProfileForm
from profiles.models import Profile, Notification
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import View
from django.db.models import Q
from django.http import HttpResponseRedirect


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
                'saved_recipes': saved_recipes,
                'posted_recipes': posted_recipes,
                'profile': get_user.profile
            },
        )


class EditProfile(View):
    """""" 
    def get(self, request, profile, *args, **kwargs):
        get_user = User.objects.get(username=profile)

        profile_form = ProfileForm(instance=get_user.profile)
        
        return render(
            request,
            'edit_profile.html',
            {
                'profile_form': profile_form,
                'profile': get_user.profile
            })

    def post(self, request, profile, *args, **kwargs):
        get_user = User.objects.get(username=profile)

        profile_form = ProfileForm(data=request.POST or None, instance=get_user.profile)

        if profile_form.is_valid():
            # https://www.geeksforgeeks.org/multiplechoicefield-django-forms/
            profile_form.save()

            return render(request, 'profile.html',
            {
                'profile': get_user.profile
            })
        else:
            return render(
                request,
                'edit_profile.html',
                {
                    'profile_form': profile_form,
                    'profile': get_user.profile
                })


def dismiss_notification(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id)
    
    if request.user.profile == notification.to:
        notification.dismissed = True
        notification.save()

    # https://stackoverflow.com/questions/50006147/how-to-return-redirect-to-previous-page-in-django-after-post-request
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
