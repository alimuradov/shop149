# Generated by Django 2.2.2 on 2019-06-27 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_title', models.CharField(blank=True, max_length=60, verbose_name='Заголовок страницы в браузере')),
                ('meta_description', models.CharField(blank=True, max_length=180, verbose_name='Описание страницы в браузере')),
                ('meta_keywords', models.CharField(blank=True, max_length=512, verbose_name='ключевые слова')),
                ('title', models.CharField(max_length=128, verbose_name='Заголовок странциы')),
                ('body', models.TextField(verbose_name='Текст страницы')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Изменено')),
                ('slug', models.SlugField(verbose_name='url-страницы')),
            ],
            options={
                'verbose_name': 'Страница',
                'verbose_name_plural': 'Страницы',
            },
        ),
    ]
