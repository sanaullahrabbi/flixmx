# Generated by Django 3.2.9 on 2022-02-07 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20220207_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviemodel',
            name='still_path',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]