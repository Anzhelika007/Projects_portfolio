from django.contrib import admin

from base.models import CategoryWord, Word, IrregularVerbs


@admin.register(CategoryWord)
class CategoryWordAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name',)
    search_fields = ('name',)
    ordering = ('-name',)


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('id', 'english', 'translate', 'category')
    fields = ('english', 'translate', 'category')
    search_fields = ('english',)
    ordering = ('category',)


@admin.register(IrregularVerbs)
class IrregularVerbsAdmin(admin.ModelAdmin):
    list_display = ('id', 'english', 'past_simple', 'past_participle', 'translate')
    fields = ('english', 'past_simple', 'past_participle', 'translate', 'category')
    search_fields = ('english',)
    ordering = ('category',)
