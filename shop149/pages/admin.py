from django_summernote.admin import SummernoteModelAdmin

from django.contrib import admin

from .models import Page


class PageAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)
    list_display = (
        'title',
        'slug',
        'modified',
    )

    search_fields = (
        'page_title',
        'body',
    )


    readonly_fields = (
        'created',
        'modified',
    )

    fieldsets = (
            (None, {
                'fields': (
                    'title',
                    'slug',
                    'body',
                ),
            }),
            ('СЕО-оптимизация', {
                'fields': (
                    'page_title',
                    'meta_description',
                    'meta_keywords',
                ),
                'classes': (
                    'collapse',
                ),
            }),
            ('Дополнительно', {
                'fields': (
                    'created',
                    'modified',
                ),
                'classes': (
                    'collapse',
                ),
            }),
        )

admin.site.register(Page, PageAdmin)

