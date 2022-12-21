from . import views
from django.urls import path
from multiurl import multiurl
from django.http import Http404
from multiurl import ContinueResolving


urlpatterns = [multiurl(
    path('<profile>/', views.ProfilePage.as_view(), name='profile_page'),
    path('dismiss/<notification_id>', views.dismiss_notification, name='dismiss_notification'),
)]