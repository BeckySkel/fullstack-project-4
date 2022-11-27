from django.contrib import admin
from .models import Recipe


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