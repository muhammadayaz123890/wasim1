# Generated by Django 4.1.7 on 2023-10-10 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=100, verbose_name='Product Category'),
        ),
    ]
