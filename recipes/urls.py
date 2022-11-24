from . import views
from django.urls import path


urlpatterns = [
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
]