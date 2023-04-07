from django.contrib import admin
from base.models import Category, Word, IrregularVerbs, Themes, LinkRender


@admin.register(Themes)
class ThemeAdmin(admin.ModelAdmin):
    list_filter = ['name', 'priority']
    list_display = ('name', 'priority')
    fields = ('name', 'priority')
    search_fields = ('name',)
    ordering = ('-name',)


@admin.register(LinkRender)
class LinkRenderAdmin(admin.ModelAdmin):
    list_filter = ['link']
    list_display = ('link',)
    fields = ('link',)
    search_fields = ('link',)
    ordering = ('link',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'theme')
    fields = ('name', 'theme', 'link')
    search_fields = ('name',)
    ordering = ('-name',)


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_filter = ['category', 'frequency_word']
    list_display = ('english', 'translate', 'category', 'frequency_word')
    fields = ('english', 'translate', 'category', 'frequency_word')
    search_fields = ('english',)
    ordering = ('category',)


@admin.register(IrregularVerbs)
class IrregularVerbsAdmin(admin.ModelAdmin):
    list_display = ('english', 'past_simple', 'past_participle', 'translate', 'frequency_word')
    fields = ('english', 'past_simple', 'past_participle', 'translate', 'category', 'frequency_word')
    search_fields = ('english',)
    ordering = ('category',)
