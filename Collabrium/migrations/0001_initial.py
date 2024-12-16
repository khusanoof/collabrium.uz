<<<<<<< HEAD
# Generated by Django 5.0.6 on 2024-12-16 13:18
=======
# Generated by Django 5.1.4 on 2024-12-15 13:37
>>>>>>> 3202a9beea2677d2591beb30171606e08195aff2

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_cover', models.ImageField(upload_to='blog_images', verbose_name='Обложка изображения')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата публикации')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок статьи')),
                ('title_uz', models.CharField(max_length=255, null=True, verbose_name='Заголовок статьи')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='Заголовок статьи')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Заголовок статьи')),
                ('page_slug', models.SlugField(unique=True, verbose_name='Слаг страницы')),
                ('main_title', models.CharField(max_length=200, verbose_name='Основной заголовок')),
                ('main_title_uz', models.CharField(max_length=200, null=True, verbose_name='Основной заголовок')),
                ('main_title_en', models.CharField(max_length=200, null=True, verbose_name='Основной заголовок')),
                ('main_title_ru', models.CharField(max_length=200, null=True, verbose_name='Основной заголовок')),
                ('text_first', ckeditor.fields.RichTextField(verbose_name='Текст 1')),
                ('text_first_uz', ckeditor.fields.RichTextField(null=True, verbose_name='Текст 1')),
                ('text_first_en', ckeditor.fields.RichTextField(null=True, verbose_name='Текст 1')),
                ('text_first_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Текст 1')),
                ('text_second', ckeditor.fields.RichTextField(verbose_name='Текст 2')),
                ('text_second_uz', ckeditor.fields.RichTextField(null=True, verbose_name='Текст 2')),
                ('text_second_en', ckeditor.fields.RichTextField(null=True, verbose_name='Текст 2')),
                ('text_second_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Текст 2')),
                ('image_first', models.ImageField(blank=True, null=True, upload_to='blog_images', verbose_name='Первое изображение')),
                ('image_second', models.ImageField(blank=True, null=True, upload_to='blog_images', verbose_name='Второе изображение')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блог',
            },
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Заголовок')),
                ('title_uz', models.CharField(max_length=300, null=True, verbose_name='Заголовок')),
                ('title_en', models.CharField(max_length=300, null=True, verbose_name='Заголовок')),
                ('title_ru', models.CharField(max_length=300, null=True, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('text_uz', models.TextField(null=True, verbose_name='Текст')),
                ('text_en', models.TextField(null=True, verbose_name='Текст')),
                ('text_ru', models.TextField(null=True, verbose_name='Текст')),
                ('page_slug', models.SlugField(verbose_name='Слаг страницы')),
            ],
            options={
                'verbose_name': 'Часто задаваемые вопросы',
                'verbose_name_plural': 'Часто задаваемые вопросы',
            },
        ),
        migrations.CreateModel(
            name='OurTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('name_uz', models.CharField(max_length=200, null=True, verbose_name='Имя')),
                ('name_en', models.CharField(max_length=200, null=True, verbose_name='Имя')),
                ('name_ru', models.CharField(max_length=200, null=True, verbose_name='Имя')),
                ('image', models.ImageField(upload_to='OurTeam_images', verbose_name='изображение')),
                ('job', models.CharField(max_length=200, verbose_name='Работа')),
                ('job_uz', models.CharField(max_length=200, null=True, verbose_name='Работа')),
                ('job_en', models.CharField(max_length=200, null=True, verbose_name='Работа')),
                ('job_ru', models.CharField(max_length=200, null=True, verbose_name='Работа')),
                ('description', models.TextField(verbose_name='описание')),
                ('description_uz', models.TextField(null=True, verbose_name='описание')),
                ('description_en', models.TextField(null=True, verbose_name='описание')),
                ('description_ru', models.TextField(null=True, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'Наша команда',
                'verbose_name_plural': 'Наша команда',
            },
        ),
        migrations.CreateModel(
            name='Podkast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.CharField(max_length=200, verbose_name='инструмент')),
                ('total_uz', models.CharField(max_length=200, null=True, verbose_name='инструмент')),
                ('total_en', models.CharField(max_length=200, null=True, verbose_name='инструмент')),
                ('total_ru', models.CharField(max_length=200, null=True, verbose_name='инструмент')),
                ('image', models.ImageField(upload_to='Images/podkast', verbose_name='изображение')),
            ],
            options={
                'verbose_name': 'Подкаст',
                'verbose_name_plural': 'Подкасты',
            },
        ),
        migrations.CreateModel(
            name='Rezident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('name_uz', models.CharField(max_length=200, null=True, verbose_name='Имя')),
                ('name_en', models.CharField(max_length=200, null=True, verbose_name='Имя')),
                ('name_ru', models.CharField(max_length=200, null=True, verbose_name='Имя')),
                ('image', models.ImageField(upload_to='rezident_images', verbose_name='изображение')),
                ('job', models.CharField(max_length=200, verbose_name='Работа')),
                ('job_uz', models.CharField(max_length=200, null=True, verbose_name='Работа')),
                ('job_en', models.CharField(max_length=200, null=True, verbose_name='Работа')),
                ('job_ru', models.CharField(max_length=200, null=True, verbose_name='Работа')),
                ('description', models.TextField(verbose_name='описание')),
                ('description_uz', models.TextField(null=True, verbose_name='описание')),
                ('description_en', models.TextField(null=True, verbose_name='описание')),
                ('description_ru', models.TextField(null=True, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'Резидент',
                'verbose_name_plural': 'Резидент',
            },
        ),
        migrations.CreateModel(
            name='Space',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('space', models.CharField(max_length=300, verbose_name='зоны')),
                ('space_uz', models.CharField(max_length=300, null=True, verbose_name='зоны')),
                ('space_en', models.CharField(max_length=300, null=True, verbose_name='зоны')),
                ('space_ru', models.CharField(max_length=300, null=True, verbose_name='зоны')),
                ('page_slug', models.SlugField(blank=True, editable=False, unique=True, verbose_name='Слаг страницы')),
                ('image', models.ImageField(upload_to='Images/space', verbose_name='изображение')),
            ],
            options={
                'verbose_name': 'Зоны',
                'verbose_name_plural': 'Зоны',
            },
        ),
    ]
