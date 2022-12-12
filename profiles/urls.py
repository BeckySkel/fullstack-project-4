from . import views
from django.urls import path
from multiurl import multiurl
from django.http import Http404
from multiurl import ContinueResolving


urlpatterns = [multiurl(
    path('<profile_id>/', views.ProfilePage.as_view(), name='profile_page'),
)]