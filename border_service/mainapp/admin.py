# mainapp/admin.py
from django.contrib import admin
from .models import News, Leader, Vacancy
from ckeditor.widgets import CKEditorWidget
from django import forms


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date', 'is_published', 'is_important']
    list_filter = ['is_published', 'is_important', 'pub_date']
    search_fields = ['title', 'content']
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ['is_published', 'is_important']
    date_hierarchy = 'pub_date'
    readonly_fields = ['pub_date']

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'content', 'image', 'pub_date')
        }),
        ('Публикация', {
            'fields': ('is_published', 'is_important'),
            'description': '«Важное объявление» будет показано на главной странице'
        }),
    )


@admin.register(Leader)
class LeaderAdmin(admin.ModelAdmin):
    list_display = ['rank', 'full_name', 'position', 'sort_order']
    list_editable = ['sort_order']
    search_fields = ['full_name', 'rank']
    list_filter = ['position']


# вакансии
@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['title', 'salary_from', 'contact_phone', 'is_published', 'sort_order']
    list_editable = ['sort_order', 'is_published']
    search_fields = ['title', 'requirements']