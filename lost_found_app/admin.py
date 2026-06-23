from django.contrib import admin
from .models import FoundItem, LostItem

@admin.register(FoundItem)
class FoundItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'user', 'location', 'status', 'submitted_at')  # Removed 'date'
    list_filter = ('status',)  # Removed 'date'
    search_fields = ('item_name', 'description', 'location')

@admin.register(LostItem)
class LostItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'user', 'location', 'date', 'submitted_at')
    list_filter = ('date',)
    search_fields = ('item_name', 'description', 'location')