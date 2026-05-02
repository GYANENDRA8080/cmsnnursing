from django.contrib import admin
from .models import Notice, GalleryImage, Programme


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_posted', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title']


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'uploaded_at', 'is_active']
    list_filter = ['is_active']


@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ['name', 'full_name', 'duration', 'intake', 'is_active']
