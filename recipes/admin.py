from django.contrib import admin
from .models import Recipe, Comment


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """"""
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_on', 'updated_on', 'removed')
    list_display = ('title', 'slug', 'created_on', 'removed')
    search_fields = ['title', 'caption']
    actions = [
        'remove_recipe'
        ]

    def remove_recipe(self, request, queryset):
        queryset.update(removed=True)
        

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """"""
    list_filter = ('created_on', 'removed')
    list_display = ('recipe', 'commenter', 'created_on', 'removed')
    search_fields = ['recipe', 'commenter']
    actions = [
        'remove_comment'
        ]
    
    def remove_comment(self, request, queryset):
        queryset.update(removed=True)