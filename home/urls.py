from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('browse/<slug:slug>', views.BrowseByTag.as_view(), name='browse'),
]