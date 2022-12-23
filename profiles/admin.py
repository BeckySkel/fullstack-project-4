from django.contrib import admin
from .models import Profile, Notification, Note


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """"""
    # list_display = ('full_name', 'user')
    search_fields = ['full_name', 'email', 'user']

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    """"""
    list_display = ('to', 'sender', 'sent', 'message', 'dismissed')
    search_fields = ['to', 'sent', 'message']
    list_filter = ('to', 'sender', 'sent')

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    """"""