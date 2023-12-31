# Generated by Django 3.2.20 on 2023-08-07 12:50

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(default='default', max_length=255, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.CharField(default='Subtitle text here', max_length=250),
            preserve_default=False,
        ),
    ]
