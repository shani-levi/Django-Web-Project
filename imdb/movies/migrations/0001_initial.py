# Generated by Django 4.0.4 on 2022-04-18 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, default='default.png', upload_to='')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('plot', models.TextField()),
                ('genre', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('writer', models.CharField(max_length=100)),
                ('actors', models.TextField()),
                ('year', models.CharField(max_length=100)),
            ],
        ),
    ]
