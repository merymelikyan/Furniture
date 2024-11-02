from django.contrib import admin
from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'number' ,'email', 'content', 'timestamp')
    search_fields = ('name', 'number', 'email', 'content')
    list_filter = ('timestamp',)
