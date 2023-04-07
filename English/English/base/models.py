from django.db import models


class Themes(models.Model):
    name = models.CharField(max_length=128)
    priority = models.IntegerField(default=100)

    class Meta:
        verbose_name = 'Theme'
        verbose_name_plural = 'Themes'

    def __str__(self):
        return self.name


class LinkRender(models.Model):
    link = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'

    def __str__(self):
        return self.link


class Category(models.Model):
    name = models.CharField(max_length=128)
    theme = models.ForeignKey(to=Themes, related_name='categories', on_delete=models.CASCADE, default=1)
    link = models.ManyToManyField('LinkRender', related_name='category_link')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Word(models.Model):
    english = models.CharField(max_length=128)
    translate = models.CharField(max_length=128)
    frequency_word = models.BooleanField(default=False)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)


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
