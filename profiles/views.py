from recipes.models import Recipe
from .forms import ProfileForm
from profiles.models import Profile, Notification
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import View
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



class EditProfile(LoginRequiredMixin, View):
    """""" 
    def get(self, request, *args, **kwargs):
        get_user = User.objects.get(id=request.user.id)

        profile_form = ProfileForm(instance=get_user.profile)
        
        skip = request.META.get('HTTP_REFERER').endswith('/accounts/signup/')
        
        return render(
            request,
            'edit_profile.html',
            {
                'profile_form': profile_form,
                'profile': get_user.profile,
                'skip': skip
            })

    def post(self, request, *args, **kwargs):
        get_user = User.objects.get(username=request.user)

        profile_form = ProfileForm(data=request.POST or None, instance=get_user.profile)

        skip = request.META.get('HTTP_REFERER').endswith('/accounts/signup/')

        if profile_form.is_valid():
            profile_form.save(commit=False)
            if not profile_form.instance.profile_image:
                profile_form.instance.profile_image = 'profile_placeholder'
            profile_form.save()

            return render(request, 'profile.html',
            {
                'profile': get_user.profile,
            })
        else:
            return render(
                request,
                'edit_profile.html',
                {
                    'profile_form': profile_form,
                    'profile': get_user.profile,
                    'skip': skip
                })


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
                'profile': get_user.profile,
                'small': small
            },
        )

@login_required
def dismiss_notification(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id)

    if request.user.profile == notification.to:

        notification.dismissed = True
        notification.save()

    # https://stackoverflow.com/questions/50006147/how-to-return-redirect-to-previous-page-in-django-after-post-request
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


