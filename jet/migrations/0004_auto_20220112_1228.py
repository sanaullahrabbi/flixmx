# Generated by Django 3.0.2 on 2022-01-12 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jet', '0003_auto_20210808_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='pinnedapplication',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
