from django.contrib import admin
from base.models import CategoryWord, Word, IrregularVerbs, Themes


@admin.register(Themes)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name',)
    search_fields = ('name',)
    ordering = ('-name',)


@admin.register(CategoryWord)
class CategoryWordAdmin(admin.ModelAdmin):
    list_display = ('name', 'theme')
    fields = ('name', 'theme')
    search_fields = ('name',)
    ordering = ('-name',)


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_filter = ['category', 'frequency_word']
    list_display = ('id', 'english', 'translate', 'category', 'frequency_word')
    fields = ('english', 'translate', 'category', 'frequency_word')
    search_fields = ('english',)
    ordering = ('category',)


@admin.register(IrregularVerbs)
class IrregularVerbsAdmin(admin.ModelAdmin):
    list_display = ('id', 'english', 'past_simple', 'past_participle', 'translate', 'frequency_word')
    fields = ('english', 'past_simple', 'past_participle', 'translate', 'category', 'frequency_word')
    search_fields = ('english',)
    ordering = ('category',)
