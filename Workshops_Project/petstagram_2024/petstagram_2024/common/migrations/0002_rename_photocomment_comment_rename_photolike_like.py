# Generated by Django 5.1.1 on 2024-10-07 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('photos', '0002_alter_photo_photo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PhotoComment',
            new_name='Comment',
        ),
        migrations.RenameModel(
            old_name='PhotoLike',
            new_name='Like',
        ),
    ]
