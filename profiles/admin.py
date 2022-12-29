from django.contrib import admin
from .models import Profile, Notification, Note


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Admin for Profile model
    """
    list_display = ('user', 'full_name')
    search_fields = ['bio', 'first_name', 'last_name']


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    """
    Admin for Notification model
    """
    list_display = ('to', 'sender', 'sent', 'message', 'dismissed')
    search_fields = ['message']
    list_filter = ('to', 'sender', 'sent', 'dismissed')


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    """
    Admin for Note model
    """
    list_display = ('recipe', 'profile', 'body')
    list_filter = ('recipe', 'profile')
