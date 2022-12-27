from . import views
from django.urls import path
from multiurl import multiurl
from django.http import Http404
from multiurl import ContinueResolving


urlpatterns = [multiurl(
    path('edit_profile/', views.EditProfile.as_view(), name='edit_profile'),
    path('<profile>/profile/', views.ProfilePage.as_view(), name='profile_page'),
    path('dismiss_<notification_id>', views.dismiss_notification, name='dismiss_notification')
)]
