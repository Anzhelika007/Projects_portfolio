# Generated by Django 3.2.16 on 2023-04-07 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_category_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='link',
            field=models.ManyToManyField(related_name='category_link', to='base.LinkRender'),
        ),
    ]
