# Generated by Django 4.0.5 on 2022-06-06 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_rename_flower_flowers_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='flowers',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
