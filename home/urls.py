from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('browse/<str:tag>', views.BrowseByTag.as_view(), name='browse'),
]