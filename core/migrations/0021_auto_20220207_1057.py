# Generated by Django 3.2.9 on 2022-02-07 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20220207_0229'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviemodel',
            name='tmdbid',
            field=models.BigIntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='seriesmodel',
            name='tmdbid',
            field=models.BigIntegerField(blank=True, null=True, unique=True),
        ),
    ]