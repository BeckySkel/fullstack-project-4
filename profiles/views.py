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
    """
    View to display form to edit user's profile

    profile_form: form, user can update their first name, last name,
    profile image and bio
    profile: object, profile of current user
    skip: boolean, allows user to to skip form when first registered
    """
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

        profile_form = ProfileForm(
            request.POST,
            request.FILES,
            instance=get_user.profile
            )

        skip = request.META.get('HTTP_REFERER').endswith('/accounts/signup/')

        if profile_form.is_valid():
            profile_form.save()

            recipes = Recipe.objects.filter(removed=False)
            saved_recipes = recipes.filter(saved_by=get_user.profile)
            posted_recipes = recipes.filter(author=get_user)

            return redirect(
                reverse(
                    "profile_page",
                    kwargs={'profile': get_user.profile}
                    ))
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
    """
    View to display the profile of the given user

    saved_recipes: queryset, user's saved recipes if user viewing own profile
    posted_recipes: queryset, other user's public recipes or all available
    own recipes
    profile: object, profile to view
    """
    def get(self, request, profile, *args, **kwargs):
        get_user = User.objects.get(username=profile)
        recipes = Recipe.objects.filter(removed=False)

        if request.user == get_user:
            saved_recipes = recipes.filter(saved_by=get_user.profile)
            posted_recipes = recipes.filter(author=get_user)
        else:
            saved_recipes = None
            posted_recipes = recipes.filter(author=get_user, private=False)

        return render(
            request,
            'profile.html',
            {
                'saved_recipes': saved_recipes,
                'posted_recipes': posted_recipes,
                'profile': get_user.profile
            },
        )


@login_required
def dismiss_notification(request, notification_id):
    """
    Quick view to dismiss notifications form user's profile page.
    Returns to current page
    """
    notification = get_object_or_404(Notification, id=notification_id)

    if request.user.profile == notification.to:
        notification.dismissed = True
        notification.save()

    # How to return to same page
    # https://stackoverflow.com/questions/50006147/how-to-return-redirect-to-previous-page-in-django-after-post-request
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
