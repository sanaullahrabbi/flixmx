# Generated by Django 3.2.7 on 2021-09-25 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210920_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='seriesmodel',
            name='tmdb_poster',
            field=models.URLField(blank=True, max_length=999, null=True),
        ),
        migrations.AddField(
            model_name='seriesmodel',
            name='tmdb_thumbnail',
            field=models.URLField(blank=True, max_length=999, null=True),
        ),
        migrations.AlterField(
            model_name='moviemodel',
            name='genre',
            field=models.ManyToManyField(max_length=250, to='core.GenreModel'),
        ),
        migrations.AlterField(
            model_name='moviemodel',
            name='slug',
            field=models.SlugField(editable=False, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='moviemodel',
            name='title',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='moviemodel',
            name='type',
            field=models.CharField(choices=[('english', 'English'), ('malayalam', 'Malayalam'), ('hindi', 'Hindi'), ('tamil', 'Tamil'), ('telegu', 'Telegu'), ('kannada', 'Kannada'), ('indian_bangla', 'Indian Bangla'), ('korean', 'Korean'), ('spanish', 'Spanish'), ('japanese', 'Japanese'), ('turkish', 'Turkish'), ('chinese', 'Chinese'), ('indonesian', 'Indonesian'), ('iranian', 'Iranian'), ('french', 'French'), ('german', 'German'), ('thai', 'Thai'), ('russian', 'Russian'), ('others', 'Others'), ('animation', 'Animation'), ('anime', 'Anime')], default='English', max_length=50, null=True),
        ),
    ]
