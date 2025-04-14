from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'rating', 'created_at', 'is_published')
    list_filter = ('rating', 'is_published')
    search_fields = ('name', 'email', 'message')
    list_editable = ('is_published',)
    date_hierarchy = 'created_at'

