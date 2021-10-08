# Generated by Django 3.2.7 on 2021-09-15 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_seasonmodel_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='episodemodel',
            name='direct_download',
            field=models.URLField(blank=True, max_length=999, null=True),
        ),
        migrations.AddField(
            model_name='moviemodel',
            name='direct_download',
            field=models.URLField(blank=True, max_length=999, null=True),
        ),
        migrations.AddField(
            model_name='softwaresgamesmodel',
            name='direct_download',
            field=models.URLField(blank=True, max_length=999, null=True),
        ),
    ]
