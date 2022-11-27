from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """"""
    list_filter = ('joined_on',)
    list_display = ('full_name', 'user', 'email', 'joined_on')
    search_fields = ['full_name', 'email']
