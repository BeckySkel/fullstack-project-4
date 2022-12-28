from . import views
from django.urls import path
from multiurl import multiurl
from django.http import Http404


urlpatterns = [multiurl(
    path('add_recipe/', views.AddRecipe.as_view(), name='add_recipe'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('<slug:slug>/edit', views.EditRecipe.as_view(), name='edit_recipe'),
    path('<slug:slug>/delete', views.delete_recipe, name='delete_recipe'),
    path('<slug:slug>/like', views.RecipeLike.as_view(), name='recipe_like'),
    path('<slug:slug>/save', views.RecipeSave.as_view(), name='recipe_save'),
    path('delete_comment/<comment_id>', views.delete_comment, name='delete_comment'),
    path('delete_note/<note_id>', views.delete_note, name='delete_note'),
)]
