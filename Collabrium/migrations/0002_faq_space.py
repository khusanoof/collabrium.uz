from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Collabrium', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('text', models.TextField()),
                ('page_slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Space',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('space', models.CharField(max_length=300)),
                ('page_slug', models.SlugField(unique=True)),
                ('image', models.URLField()),
            ],
        ),
    ]