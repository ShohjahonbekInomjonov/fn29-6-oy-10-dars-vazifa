from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Genre, Movie, Comment

# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    readonly_fields = ('created',)


class MovieAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'genre', 'year', 'get_image', 'views')
    list_filter = ('genre', 'year')
    search_fields = ('title', 'description')
    ordering = ('-year',)
    list_editable = ('year', 'genre')
    list_display_links = ('pk', 'title')
    inlines = [
        CommentInline
    ]
    fieldsets = (
        (
            "Asosiy ma'lumotlar", {
                'fields': ('title', 'genre')
            }),
        ("qo'shimcha ma'lumotlar", {
            'fields': ('year', 'description', 'photo', 'video', 'views'),
            'classes': ('collapse',),
        }),
    )

    def get_image(self, obj: Movie):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width=60px>')
        return '-'


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)