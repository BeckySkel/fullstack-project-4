from django.contrib import admin
from .models import Profile, Notification


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """"""
    list_display = ('full_name', 'user')
    search_fields = ['full_name', 'email']

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    """"""
    # list_display = ('full_name', 'user')
    # search_fields = ['full_name', 'email']