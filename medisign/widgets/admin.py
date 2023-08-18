from django.contrib import admin
from .models import Widget

class WidgetAdmin(admin.ModelAdmin):
    list_display = ('text', 'user')  # columns to be displayed in the list view
    search_fields = ['text', 'user__username']  # fields that will be searched upon
    list_filter = ('user',)  # create a filter sidebar to filter by user

admin.site.register(Widget, WidgetAdmin)
