from .models import GenreModel
from django.conf import settings
def site(request):
    return {'SITE_URL': settings.SITE_URL}

def servemodels(request):
    genres = GenreModel.objects.all()
    genresList = [genres[i:i+7] for i in range(0,len(genres),7)]
    context = {
        'genresList':genresList
    }
    return context