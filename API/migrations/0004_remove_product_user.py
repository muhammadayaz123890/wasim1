# Generated by Django 4.1.7 on 2023-10-10 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_product_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
    ]