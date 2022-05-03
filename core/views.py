from itertools import chain

from django.http import HttpResponse
from core.models import *
from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
import random
from urllib.parse import *

# Create your views here.
def index(request):
    # topsliderobjs = TopSlideModel.objects.filter()
    topsliderobjs = sorted(TopSlideModel.objects.filter(), key=lambda x: random.random())
    topmovieobjs = MovieModel.objects.filter().order_by('-created_at')[:50]
    engmovieobjs = MovieModel.objects.filter(type='english').order_by('-release_date')
    frgmovieobjs = MovieModel.objects.filter(Q(type='korean')|Q(type='spanish')|Q(type='japanese')|Q(type='turkish')|Q(type='chinese')|Q(type='thai')|Q(type='russian')|Q(type='indonesian')|Q(type='iranian')|Q(type='french')|Q(type='german')|Q(type='others')).order_by('-release_date')
    hindimovieobjs = MovieModel.objects.filter(type='hindi').order_by('-release_date')
    southmovieobjs = MovieModel.objects.filter(Q(type='malayalam')|Q(type='tamil')|Q(type='telegu')|Q(type='kannada')).order_by('-release_date')
    # dualaudioobjs = DualAudioModel.objects.filter().order_by('-movie_content__created_at')
    dualaudioobjs = DualAudioModel.objects.filter().order_by('-movie_content__release_date')

    seriesobjs = SeriesModel.objects.filter().order_by('-release_date').exclude(Q(type='korean')|Q(type='anime'))
    kdramaobjs = SeriesModel.objects.filter(type='korean').order_by('-release_date')
    
    animationobjs = MovieModel.objects.filter(type='animation').order_by('-release_date')
    animemovieobjs = MovieModel.objects.filter(type='anime').order_by('-release_date')
    animeseriesobjs = SeriesModel.objects.filter(type='anime').order_by('-release_date')

    # softwaresobjs = SoftwaresGamesModel.objects.filter(category='softwares').order_by('-release_date')
    # gamesobjs = SoftwaresGamesModel.objects.filter(category='games').order_by('-release_date')
    bsubmakerobjs = BsubCreatorModel.objects.all()
    specialobj = SpecialModel.objects.first().movie_content
    context = {
        'topsliderobjs':topsliderobjs,
        'topmovieobjs':topmovieobjs,

        'engmovieobjs':engmovieobjs,
        'hindimovieobjs':hindimovieobjs,
        'southmovieobjs':southmovieobjs,
        'frgmovieobjs':frgmovieobjs,
        'dualaudioobjs':dualaudioobjs,

        'seriesobjs':seriesobjs,
        'kdramaobjs':kdramaobjs,

        'animationobjs':animationobjs,
        'animemovieobjs':animemovieobjs,
        'animeseriesobjs':animeseriesobjs,

        # 'softwaresobjs':softwaresobjs,
        # 'gamesobjs':gamesobjs,
        'specialobj':specialobj,
        'bsubmakerobjs':bsubmakerobjs,
    }
    return render(request,'core/index.html',context)

def movies_view(request,type):
    if type=='foreign':
        movies = MovieModel.objects.filter(Q(type='korean')|Q(type='spanish')|Q(type='japanese')|Q(type='turkish')|Q(type='chinese')|Q(type='thai')|Q(type='russian')|Q(type='indonesian')|Q(type='iranian')|Q(type='french')|Q(type='german')|Q(type='others')).order_by('-release_date')
    elif type=='south_indian':
        movies = MovieModel.objects.filter(Q(type='malayalam')|Q(type='tamil')|Q(type='telegu')|Q(type='kannada')).order_by('-release_date')
    else:
        movies = MovieModel.objects.filter(type=type).order_by('-release_date')
    paginator = Paginator(movies,20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'movies':page_obj,
        'type':type,
        'totalobj':movies.count,
    }
    return render(request,'core/all/movies.html',context)

def series_view(request,type):
    if type=='all':
        series = SeriesModel.objects.filter().order_by('-release_date').exclude(type='korean')
    elif type=='indian':
        series = SeriesModel.objects.filter(Q(type='malayalam')|Q(type='hindi')|Q(type='tamil')|Q(type='telegu')|Q(type='kannada')).order_by('-release_date')
    elif type=='foreign':
        series = SeriesModel.objects.filter(Q(type='spanish')|Q(type='japanese')|Q(type='turkish')|Q(type='chinese')|Q(type='thai')|Q(type='russian')|Q(type='indonesian')|Q(type='iranian')|Q(type='french')|Q(type='german')|Q(type='others')).order_by('-release_date')
    else:
        series = SeriesModel.objects.filter(type=type).order_by('-release_date')
        
    paginator = Paginator(series,20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'series':page_obj,
        'type':type,
        'totalobj':series.count,
    }
    return render(request,'core/all/series.html',context)

def softwaresGames_view(request,category):
    softwaresGames = SoftwaresGamesModel.objects.filter(category=category).order_by('-created_at')
    paginator = Paginator(softwaresGames,20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'softwaresGames':page_obj,
        'category':category,
        'totalobj':softwaresGames.count,
    }
    return render(request,'core/all/softwaresgames.html',context)

def genres_view(request,genrename):
    genrename = unquote(genrename)
    movies = MovieModel.objects.filter(genre__genre_name__icontains=genrename).order_by('-release_date')
    paginator = Paginator(movies,20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'movies':page_obj,
        'genrename':genrename,
        'totalobj':movies.count,
    }
    return render(request,'core/all/genres.html',context)

def classic_view(request,type):
    classicmovies = ClassicModel.objects.filter(type=type)
    paginator = Paginator(classicmovies,20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'classicmovies':page_obj,
        'type':type,
        'totalobj':classicmovies.count,
    }
    return render(request,'core/all/classic.html',context)

def dualaudio_view(request):
    dualaudiomovies = DualAudioModel.objects.all()
    paginator = Paginator(dualaudiomovies,20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'dualaudiomovies':page_obj,
        'totalobj':dualaudiomovies.count,
    }
    return render(request,'core/special/dual_audio.html',context)

def bsub_view(request):
    bsubmovies = BSubModel.objects.all()
    paginator = Paginator(bsubmovies,20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'bsubmovies':page_obj,
        'totalobj':bsubmovies.count,
    }
    return render(request,'core/special/bsub.html',context)

def hindidubbed_view(request):
    hindidubbedmovies = HindiDubbedModel.objects.all()
    paginator = Paginator(hindidubbedmovies,20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'hindidubbedmovies':page_obj,
        'totalobj':hindidubbedmovies.count,
    }
    return render(request,'core/special/hindi_dubbed.html',context)
    
def satyajitray_view(request):
    satyajitraymovies = SatyajitRayModel.objects.all()
    paginator = Paginator(satyajitraymovies,20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'satyajitraymovies':page_obj,
        'totalobj':satyajitraymovies.count,
    }
    return render(request,'core/special/satyajitray.html',context)

def jamesbond_view(request):
    jamesbondmovies = JamesBondModel.objects.all()
    paginator = Paginator(jamesbondmovies,20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'jamesbondmovies':page_obj,
        'totalobj':jamesbondmovies.count,
    }
    return render(request,'core/special/jamesbond.html',context)

def oscarwinning_view(request):
    oscarwinningmovies = OscarWinningModel.objects.all()
    paginator = Paginator(oscarwinningmovies,20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'oscarwinningmovies':page_obj,
        'totalobj':oscarwinningmovies.count,
    }
    return render(request,'core/special/oscarwinning.html',context)

def imdbtop_view(request):
    imdbtopmovies = IMDBTopModel.objects.all()
    paginator = Paginator(imdbtopmovies,20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'imdbtopmovies':page_obj,
        'totalobj':imdbtopmovies.count,
    }
    return render(request,'core/special/imdbtop.html',context)

def superhero_view(request):
    superheromovies = SuperheroModel.objects.all()
    paginator = Paginator(superheromovies,20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'superheromovies':page_obj,
        'totalobj':superheromovies.count,
    }
    return render(request,'core/special/superhero.html',context)

def details_movie_view(request,pk):
    obj = MovieModel.objects.get(slug = pk)
    recobjs = sorted(MovieModel.objects.filter(type=obj.type).order_by('-created_at')[:12], key=lambda x: random.random())
    context = {
        'obj':obj,
        'recobjs':recobjs
    }
    return render(request,'core/details/details_movie.html',context)

def director_contents_view(request,directorName):
    directorName = unquote(directorName)
    movies = MovieModel.objects.filter(director__icontains = directorName).order_by('-release_date')
    paginator = Paginator(movies,20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'movies':page_obj,
        'director':directorName,
        'totalobj':movies.count,
    }
    return render(request,'core/all/director_contents.html',context)

def writer_contents_view(request,writerName):
    writerName = unquote(writerName)
    movies = MovieModel.objects.filter(writers__icontains = writerName).order_by('-release_date')
    paginator = Paginator(movies,20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'movies':page_obj,
        'writer':writerName,
        'totalobj':movies.count,
    }
    return render(request,'core/all/writer_contents.html',context)

def actor_contents_view(request,actorName):
    actorName = unquote(actorName)
    movies = MovieModel.objects.filter(starring__icontains = actorName).order_by('-release_date')
    paginator = Paginator(movies,20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'movies':page_obj,
        'actor':actorName,
        'totalobj':movies.count,
    }
    return render(request,'core/all/actor_contents.html',context)

def bsubcreator_contents_view(request,creatorSlug):
    movies = MovieModel.objects.filter(bsub_creator__slug = creatorSlug).order_by('-release_date')
    series = SeriesModel.objects.filter(bsub_creator__slug = creatorSlug).order_by('-release_date')
    creator = BsubCreatorModel.objects.filter(slug=creatorSlug)[0]
    objs = sorted(list(chain(movies,series)), key=lambda x: random.random())
    paginator = Paginator(objs,20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'movies':page_obj,
        'creator':creator,
        'totalobj':objs.__len__,
    }
    return render(request,'core/all/bsubcreator_contents.html',context)

def details_series_view(request,pk):
    obj = SeriesModel.objects.get(slug = pk)
    seasons = SeasonModel.objects.filter(series__slug = pk)
    recobjs = sorted(SeriesModel.objects.filter(type=obj.type).order_by('-created_at')[:12], key=lambda x: random.random())
    context = {
        'obj':obj,
        'seasons':seasons,
        'recobjs':recobjs
    }
    return render(request,'core/details/details_series.html',context)


def details_season_view(request,pk):
    obj = SeasonModel.objects.get(id = pk)
    episodes = EpisodeModel.objects.filter(season__id = pk)
    recobjs = sorted(SeasonModel.objects.filter(series__type=obj.series.type).order_by('-created_at')[:12], key=lambda x: random.random())
    context = {
        'obj':obj,
        'episodes':episodes,
        'recobjs':recobjs
    }
    return render(request,'core/details/details_season.html',context)


def details_softwaresGames_view(request,category,pk):
    obj = SoftwaresGamesModel.objects.get(slug= pk)
    recobjs = sorted(SoftwaresGamesModel.objects.filter(category=category).order_by('-created_at')[:12], key=lambda x: random.random())
    context = {
        'obj':obj,
        'recobjs':recobjs
    }
    return render(request,'core/details/details_softwaresgames.html',context)

def search_view(request):
    title = request.GET.get('title')
    movies = MovieModel.objects.filter(title__icontains = title).exclude(Q(type='animation')|Q(type='anime')).order_by('-release_date')[:50]
    series = SeriesModel.objects.filter(title__icontains = title).exclude(Q(type='korean')|Q(type='anime')).order_by('-release_date')[:50]
    animationobjs = MovieModel.objects.filter(title__icontains = title).filter(type='animation').order_by('-release_date')[:50]
    animemovieobjs = MovieModel.objects.filter(title__icontains = title).filter(type='anime').order_by('-release_date')[:50]
    animeseriesobjs = SeriesModel.objects.filter(title__icontains = title).filter(type='anime').order_by('-release_date')[:50]
    kdramaobjs = SeriesModel.objects.filter(title__icontains = title).filter(type='korean').order_by('-release_date')[:50]
    softwares = SoftwaresGamesModel.objects.filter(title__icontains = title).exclude(category='games').order_by('-release_date')[:50]
    games = SoftwaresGamesModel.objects.filter(title__icontains = title).exclude(category='softwares').order_by('-release_date')[:50]
    context = {
        'searched':title,
        'movieobjs':movies,
        'seriesobjs':series,
        'animationobjs':animationobjs,
        'animemovieobjs':animemovieobjs,
        'animeseriesobjs':animeseriesobjs,
        'kdramaobjs':kdramaobjs,
        'softwaresobjs':softwares,
        'gamesobjs':games,
    }
    return render(request,'core/search.html',context)

def contactus_view(request):
    return render(request,'core/extras/contactus.html')

def aboutus_view(request):
    return render(request,'core/extras/aboutus.html')

def privacy_view(request):
    return render(request,'core/extras/privacy.html')

def fileserver_view(request):
    return render(request,'core/fileserver.html')

# custom error handling page
def custom_page_not_found_view(request, exception=None):
    return render(request, "custom_error_page/404.html", {})

def custom_error_view(request, exception=None):
    return render(request, "custom_error_page/500.html", {})

def custom_permission_denied_view(request, exception=None):
    return render(request, "custom_error_page/403.html", {})

def custom_bad_request_view(request, exception=None):
    return render(request, "custom_error_page/400.html", {})



def testapi(request):
    return HttpResponse("Hello")