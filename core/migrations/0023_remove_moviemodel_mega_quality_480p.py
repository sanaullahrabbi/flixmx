# Generated by Django 3.2.9 on 2022-02-09 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_moviemodel_still_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviemodel',
            name='mega_quality_480p',
        ),
    ]