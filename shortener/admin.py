from django.contrib import admin
from .models import Link

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('short_code', 'original_url', 'user', 'click_count', 'created_at')
    list_filter = ('user', 'created_at')
    search_fields = ('short_code', 'original_url', 'user__username')
    readonly_fields = ('click_count', 'created_at')
    ordering = ('-created_at',)
