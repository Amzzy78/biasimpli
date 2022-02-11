# Generated by Django 3.2 on 2022-02-11 17:00

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20220209_1927'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created',
            new_name='created_on',
        ),
        migrations.AddField(
            model_name='post',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
