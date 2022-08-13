# Generated by Django 3.2.9 on 2022-08-13 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_auto_20220808_2248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('link', models.URLField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='episodemodel',
            name='hevc_download_alt1_name',
        ),
        migrations.RemoveField(
            model_name='episodemodel',
            name='hevc_download_alt1_url',
        ),
        migrations.RemoveField(
            model_name='episodemodel',
            name='hevc_download_alt2_name',
        ),
        migrations.RemoveField(
            model_name='episodemodel',
            name='hevc_download_alt2_url',
        ),
        migrations.RemoveField(
            model_name='episodemodel',
            name='hevc_download_main',
        ),
        migrations.AddField(
            model_name='seasonmodel',
            name='download_full_quality_2160p',
            field=models.URLField(blank=True, max_length=999, null=True),
        ),
    ]
