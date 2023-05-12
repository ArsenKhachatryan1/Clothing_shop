# Generated by Django 4.2.1 on 2023-05-12 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_productcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images', verbose_name='Name')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('text', models.TextField(verbose_name='Text')),
                ('price', models.CharField(max_length=50, verbose_name='Price')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cat_prod', to='main.productcategory')),
            ],
        ),
    ]