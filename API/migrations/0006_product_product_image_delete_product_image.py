# Generated by Django 4.0.2 on 2023-10-16 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0005_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.FileField(default=None, help_text='Upload Image', upload_to='product_description'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Product_Image',
        ),
    ]