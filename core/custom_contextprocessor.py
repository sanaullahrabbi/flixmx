from .models import GenreModel
from django.conf import settings
def site(request):
    return {'SITE_URL': settings.SITE_URL}

def servemodels(request):
    genres = GenreModel.objects.all()
    genresList = [genres[i:i+9] for i in range(0,len(genres),9)]
    context = {
        'genresList':genresList
    }
    return context