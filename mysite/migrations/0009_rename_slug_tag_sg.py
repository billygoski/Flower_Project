# Generated by Django 4.0.5 on 2022-06-10 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_tag_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='slug',
            new_name='sg',
        ),
    ]
