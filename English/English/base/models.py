from django.db import models


class CategoryWord(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Word(models.Model):
    english = models.CharField(max_length=128)
    translate = models.CharField(max_length=128)
    category = models.ForeignKey(to=CategoryWord, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Word'
        verbose_name_plural = 'Words'

    def __str__(self):
        return self.english


class IrregularVerbs(Word):
    past_simple = models.CharField(max_length=128)
    past_participle = models.CharField(max_length=128)
    class Meta:
        verbose_name = 'Verb'
        verbose_name_plural = 'Verbs'

    def __str__(self):
        return self.english
