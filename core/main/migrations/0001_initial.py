# Generated by Django 4.2.1 on 2023-05-12 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Copyright')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('name_link', models.CharField(max_length=50, verbose_name='Name Link')),
            ],
            options={
                'verbose_name': 'Footer',
                'verbose_name_plural': 'Footer',
            },
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('colored_title', models.CharField(max_length=50, verbose_name='Colored Title')),
                ('path1', models.CharField(max_length=50, verbose_name='Path 1')),
                ('path2', models.CharField(max_length=50, verbose_name='Path 2')),
                ('path3', models.CharField(max_length=50, verbose_name='Path 3')),
                ('path4', models.CharField(max_length=50, verbose_name='Path 4')),
                ('path5', models.CharField(max_length=50, verbose_name='Path 5')),
            ],
            options={
                'verbose_name': 'Header',
                'verbose_name_plural': 'Header',
            },
        ),
    ]
