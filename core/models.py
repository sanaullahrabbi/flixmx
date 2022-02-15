from django.db import models
from django.template.defaultfilters import slugify
from datetime import date, datetime
import uuid
from django.contrib.auth.models import User
# Create your models here.

MOVIE_TYPE = (
    ('english','English'),

    ('malayalam','Malayalam'),
    ('hindi','Hindi'),
    ('tamil','Tamil'),
    ('telegu','Telegu'),
    ('kannada','Kannada'),
    ('indian_bangla','Indian Bangla'),

    ('korean','Korean'),
    ('spanish','Spanish'),
    ('japanese','Japanese'),
    ('turkish','Turkish'),
    ('chinese','Chinese'),
    ('indonesian','Indonesian'),
    ('iranian','Iranian'),
    ('french','French'),
    ('german','German'),
    ('thai','Thai'),
    ('russian','Russian'),
    ('others','Others'),


    ('animation','Animation'),
    ('anime','Anime'),
)

GAME_PLATFORM = (
    ('pc','PC'),
    ('android','Android'),
    ('console','Console'),
)

SUBTITLE_LANGUAGE = (
    ('english','English'),
    ('bangla','Bangla'),
)

    
class GenreModel(models.Model):
    genre_name = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.genre_name}"


class MovieModel(models.Model):
    slug = models.SlugField(max_length=250,null=True,blank=True)
    tmdbid = models.BigIntegerField(unique=True,null=True,blank=True)
    title = models.CharField(max_length=250,null=True)
    description = models.TextField(null=True,blank=True)
    poster = models.ImageField(upload_to='posters',null=True,blank=True)
    tmdb_poster = models.URLField(max_length=999,null=True,blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails',null=True,blank=True)
    tmdb_thumbnail = models.URLField(max_length=999,null=True,blank=True)
    director = models.CharField(max_length=250,null=True,blank=True)
    writers = models.CharField(max_length=250,null=True,blank=True)
    starring = models.CharField(max_length=250,null=True,blank=True)
    type = models.CharField(max_length=50,null=True,choices=MOVIE_TYPE,default='English')
    genre = models.ManyToManyField(GenreModel,max_length=250)
    runtime = models.CharField(max_length=250,null=True,blank=True)
    rating = models.FloatField(null=True,blank=True)
    rated = models.CharField(max_length=250,null=True,blank=True)
    release_date = models.DateField(null=True,blank=True,default=date.today)    
    trailer_link = models.CharField(max_length=999,null=True,blank=True)

    watch_link_main_source = models.URLField(max_length=999,null=True,blank=True)
    watch_link_alt1_name = models.CharField(max_length=250,null=True,blank=True)
    watch_link_alt1_url = models.URLField(max_length=999,null=True,blank=True)
    watch_link_alt2_name = models.CharField(max_length=250,null=True,blank=True)
    watch_link_alt2_url = models.URLField(max_length=999,null=True,blank=True)

    direct_download_480p = models.URLField(max_length=999,null=True,blank=True)
    direct_download_720p = models.URLField(max_length=999,null=True,blank=True)
    direct_download_1080p = models.URLField(max_length=999,null=True,blank=True)
    direct_download_4K = models.URLField(max_length=999,null=True,blank=True)
    direct_download_dual_audio = models.URLField(max_length=999,null=True,blank=True)
    direct_download_hindi_dubbed = models.URLField(max_length=999,null=True,blank=True)

    gdrive_quality_480p = models.URLField(max_length=999,null=True,blank=True)
    gdrive_quality_720p = models.URLField(max_length=999,null=True,blank=True)
    gdrive_quality_1080p = models.URLField(max_length=999,null=True,blank=True)
    gdrive_quality_4K = models.URLField(max_length=999,null=True,blank=True)
    gdrive_download_dual_audio = models.URLField(max_length=999,null=True,blank=True)
    gdrive_download_hindi_dubbed = models.URLField(max_length=999,null=True,blank=True)

    onedrive_quality_480p = models.URLField(max_length=999,null=True,blank=True)
    onedrive_quality_720p = models.URLField(max_length=999,null=True,blank=True)
    onedrive_quality_1080p = models.URLField(max_length=999,null=True,blank=True)
    onedrive_quality_4K = models.URLField(max_length=999,null=True,blank=True)
    onedrive_download_dual_audio = models.URLField(max_length=999,null=True,blank=True)
    onedrive_download_hindi_dubbed = models.URLField(max_length=999,null=True,blank=True)

    hevc_quality_720p = models.URLField(max_length=999,null=True,blank=True)
    hevc_quality_1080p = models.URLField(max_length=999,null=True,blank=True)
    hevc_quality_4K = models.URLField(max_length=999,null=True,blank=True)
    hevc_download_dual_audio = models.URLField(max_length=999,null=True,blank=True)
    hevc_download_hindi_dubbed = models.URLField(max_length=999,null=True,blank=True)

    torrent = models.URLField(max_length=999,null=True,blank=True)

    info1 = models.CharField(max_length=250,null=True,blank=True)
    info2 = models.CharField(max_length=250,null=True,blank=True)
    synopsys = models.TextField(null=True,blank=True)
    subtitle_link = models.URLField(max_length=999,null=True,blank=True)

    still_path = models.CharField(max_length=5000,null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='create_user', on_delete=models.SET_NULL,blank=True, null=True)
    last_update = models.ForeignKey(User, related_name='update_user', on_delete=models.SET_NULL,blank=True, null=True)
    class Meta:
        ordering = ('title', )

    def __str__(self):
        return f"{self.title} #ID{self.id}" 

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.title}')
        super(MovieModel, self).save(*args, **kwargs)

    def create(self,request):
        if not self.created_by:
            self.created_by = request.user
            
    def update(self,request):
        self.last_update = request.user

    def delete(self):
        self.thumbnail.delete()
        self.poster.delete()
        super(MovieModel, self).delete()

# Create your models here.
class SeriesModel(models.Model):
    tmdbid = models.BigIntegerField(unique=True,null=True,blank=True)
    slug = models.SlugField(max_length=250,null=True,blank=True)
    title = models.CharField(max_length=250,null=True,blank=True)

    description = models.TextField(null=True,blank=True)
    tmdb_poster = models.URLField(max_length=999,null=True,blank=True)
    poster = models.ImageField(upload_to='posters/',null=True,blank=True)
    tmdb_thumbnail = models.URLField(max_length=999,null=True,blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails/',null=True,blank=True)
    
    director = models.CharField(max_length=250,null=True,blank=True)
    writers = models.CharField(max_length=250,null=True,blank=True)
    starring = models.CharField(max_length=250,null=True,blank=True)
    type = models.CharField(max_length=50,null=True,blank=True,choices=MOVIE_TYPE,default='English')
    genre = models.ManyToManyField(GenreModel,max_length=250,blank=True)
    release_date = models.DateField(null=True,blank=True,default=date.today)    
    end_date = models.DateField(null=True,blank=True)

    rating = models.FloatField(null=True,blank=True)
    rated = models.CharField(max_length=250,null=True,blank=True)
    trailer_link = models.CharField(max_length=999,null=True,blank=True)

    info1 = models.CharField(max_length=250,null=True,blank=True)
    info2 = models.CharField(max_length=250,null=True,blank=True)
    synopsys = models.TextField(null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='create_user_series', on_delete=models.SET_NULL,blank=True, null=True)
    last_update = models.ForeignKey(User, related_name='update_user_series', on_delete=models.SET_NULL,blank=True, null=True)
    class Meta:
        ordering = ('title', )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.title}')
        super(SeriesModel, self).save(*args, **kwargs)
    
    def create(self,request):
        if not self.created_by:
            self.created_by = request.user
            
    def update(self,request):
        self.last_update = request.user
        
    def delete(self):
        self.thumbnail.delete()
        self.poster.delete()
        super(MovieModel, self).delete()

class SeasonModel(models.Model):
    series = models.ForeignKey(SeriesModel,on_delete=models.CASCADE,null=True)
    slug = models.SlugField(max_length=250,null=True,blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails',null=True,blank=True)
    release_date = models.DateField(null=True,blank=True,default=date.today)
    season_number = models.IntegerField(null=True,blank=True,default=0)
    episode_count = models.IntegerField(null=True,blank=True,default=0)
    complete = models.BooleanField(default=False)

    download_full_quality_480p = models.URLField(max_length=999,null=True,blank=True)
    download_full_quality_720p = models.URLField(max_length=999,null=True,blank=True)
    download_full_quality_1080p = models.URLField(max_length=999,null=True,blank=True)
    download_full_download_dual_audio = models.URLField(max_length=999,null=True,blank=True)
    download_full_download_hindi_dubbed = models.URLField(max_length=999,null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('series__title','season_number', )
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.series.title}-season{self.season_number}')
        super(SeasonModel, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.series.title} (Season {self.season_number})"


class EpisodeModel(models.Model):
    title = models.CharField(max_length=250,null=True,blank=True)
    tmdb_thumbnail = models.URLField(max_length=999,null=True,blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails',null=True,blank=True)
    season = models.ForeignKey(SeasonModel,on_delete=models.CASCADE,null=True)
    episode = models.IntegerField(null=True,blank=True,default=0)
    description = models.TextField(null=True,blank=True)
    rating = models.FloatField(null=True,blank=True)
    runtime = models.CharField(max_length=250,null=True,blank=True)

    watch_link_main_source = models.URLField(max_length=999,null=True,blank=True)
    watch_link_alt1_name = models.CharField(max_length=250,null=True,blank=True)
    watch_link_alt1_url = models.URLField(max_length=999,null=True,blank=True)
    watch_link_alt2_name = models.CharField(max_length=250,null=True,blank=True)
    watch_link_alt2_url = models.URLField(max_length=999,null=True,blank=True)

    direct_download_main = models.URLField(max_length=999,null=True,blank=True)
    direct_download_alt1_name = models.CharField(max_length=250,null=True,blank=True)
    direct_download_alt1_url = models.URLField(max_length=999,null=True,blank=True)
    direct_download_alt2_name = models.CharField(max_length=250,null=True,blank=True)
    direct_download_alt2_url = models.URLField(max_length=999,null=True,blank=True)

    gdrive_download_main = models.URLField(max_length=999,null=True,blank=True)
    gdrive_download_alt1_name = models.CharField(max_length=250,null=True,blank=True)
    gdrive_download_alt1_url = models.URLField(max_length=999,null=True,blank=True)
    gdrive_download_alt2_name = models.CharField(max_length=250,null=True,blank=True)
    gdrive_download_alt2_url = models.URLField(max_length=999,null=True,blank=True)

    onedrive_download_main = models.URLField(max_length=999,null=True,blank=True)
    onedrive_download_alt1_name = models.CharField(max_length=250,null=True,blank=True)
    onedrive_download_alt1_url = models.URLField(max_length=999,null=True,blank=True)
    onedrive_download_alt2_name = models.CharField(max_length=250,null=True,blank=True)
    onedrive_download_alt2_url = models.URLField(max_length=999,null=True,blank=True)

    hevc_download_main = models.URLField(max_length=999,null=True,blank=True)
    hevc_download_alt1_name = models.CharField(max_length=250,null=True,blank=True)
    hevc_download_alt1_url = models.URLField(max_length=999,null=True,blank=True)
    hevc_download_alt2_name = models.CharField(max_length=250,null=True,blank=True)
    hevc_download_alt2_url = models.URLField(max_length=999,null=True,blank=True)

    subtitle_link = models.URLField(max_length=999,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('season', )
    def __str__(self):
        return f"{self.season} (Episode {self.episode})"

    def save(self, *args, **kwargs):
        if not self.id:
            season = SeasonModel.objects.get(id = self.season_id)
            season.episode_count = self.season.episodemodel_set.count()+1
            season.save()
        super(EpisodeModel, self).save(*args, **kwargs)



class SoftwaresGamesModel(models.Model):
    CATEGORY = (
        ('softwares','Softwares'),
        ('games','Games'),
        ('ebooks','eBooks'),
        ('tutorials','Tutorials')
    )

    title = models.CharField(max_length=250,null=True,blank=True)
    slug = models.SlugField(max_length=250,null=True,blank=True)
    poster = models.ImageField(upload_to='posters/',null=True,blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails/',null=True,blank=True)

    category = models.CharField(max_length=50,null=True,blank=True,choices=CATEGORY,default='Games')
    platform = models.CharField(max_length=50,null=True,blank=True,choices=GAME_PLATFORM,default='PC')

    rated = models.CharField(max_length=250,null=True,blank=True)
    size = models.CharField(max_length=250,null=True,blank=True)
    release_date = models.DateField(null=True,blank=True,default=date.today)
    genre = models.ManyToManyField(GenreModel,max_length=250,blank=True)
    developer = models.CharField(max_length=250,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    min_sys_req = models.TextField(null=True,blank=True)
    rec_sys_req = models.TextField(null=True,blank=True)
    general_notes = models.TextField(null=True,blank=True)

    direct_download = models.URLField(max_length=999,null=True,blank=True)
    gdrive_download_link = models.URLField(max_length=999,null=True,blank=True)
    onedrive_download_link = models.URLField(max_length=999,null=True,blank=True)
    torrent = models.URLField(max_length=999,null=True,blank=True)

    info1 = models.CharField(max_length=250,null=True,blank=True)
    info2 = models.CharField(max_length=250,null=True,blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='create_user_sge', on_delete=models.SET_NULL,blank=True, null=True)
    last_update = models.ForeignKey(User, related_name='update_user_sge', on_delete=models.SET_NULL,blank=True, null=True)
    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return f"{self.title} #ID{self.id}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.title}')
        super(SoftwaresGamesModel, self).save(*args, **kwargs)


class TopSlideModel(models.Model):
    movie_content = models.ForeignKey(MovieModel,on_delete=models.SET_NULL,null=True,blank=True)
    series_content = models.ForeignKey(SeriesModel,on_delete=models.SET_NULL,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-created_at', )
    def __str__(self):
        if self.movie_content and  self.series_content:
            return f"{self.movie_content} | {self.series_content}"
        elif self.movie_content and not self.series_content:
            return f"{self.movie_content}" 
        elif self.series_content and not self.movie_content:
            return f"{self.series_content}"
        else:
            return self.id



class BSubModel(models.Model):
    movie_content = models.ForeignKey(MovieModel,on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-created_at', )
    def __str__(self):
        return f"{self.movie_content}" 

class ClassicModel(models.Model):
    CATEGORY = (
        ('hollywood','Hollywood'),
        ('bollywood','Bollywood'),
        ('horror','Horror'),
        ('foreign','Foreign')
    )
    movie_content = models.ForeignKey(MovieModel,on_delete=models.SET_NULL,null=True)
    type = models.CharField(max_length=50,null=True,blank=True,choices=CATEGORY,default='hollywood')

    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-created_at', )
    def __str__(self):
        return f"{self.movie_content}" 

class SatyajitRayModel(models.Model):
    movie_content = models.ForeignKey(MovieModel,on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-created_at', )
    def __str__(self):
        return f"{self.movie_content}" 

class JamesBondModel(models.Model):
    movie_content = models.ForeignKey(MovieModel,on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-created_at', )
    def __str__(self):
        return f"{self.movie_content}" 

class DualAudioModel(models.Model):
    movie_content = models.ForeignKey(MovieModel,on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-created_at', )
    def __str__(self):
        return f"{self.movie_content}" 

class HindiDubbedModel(models.Model):
    movie_content = models.ForeignKey(MovieModel,on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-created_at', )
    def __str__(self):
        return f"{self.movie_content}" 
        
class IMDBTopModel(models.Model):
    movie_content = models.ForeignKey(MovieModel,on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-created_at', )
    def __str__(self):
        return f"{self.movie_content}" 

class OscarWinningModel(models.Model):
    movie_content = models.ForeignKey(MovieModel,on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-created_at', )
    def __str__(self):
        return f"{self.movie_content}" 

class SuperheroModel(models.Model):
    movie_content = models.ForeignKey(MovieModel,on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-created_at', )
    def __str__(self):
        return f"{self.movie_content}" 



class SpecialModel(models.Model):
    movie_content = models.ForeignKey(MovieModel,on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movie_content}" 


# uuid = models.UUIDField(default=uuid.uuid4,null=True,unique=True,editable=False)
