# Generated by Django 4.0.2 on 2022-02-23 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_category_subcategory_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image2_url',
        ),
    ]
