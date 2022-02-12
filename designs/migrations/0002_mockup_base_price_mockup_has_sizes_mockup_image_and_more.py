# Generated by Django 4.0.2 on 2022-02-11 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mockup',
            name='base_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mockup',
            name='has_sizes',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='mockup',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='mockup',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
