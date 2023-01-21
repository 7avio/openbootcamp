from django.shortcuts import render
from .models import Director, Movie
from django.http import HttpResponse

#
def index(request):
    directors = Director.objects.all()
    context = {'directors': directors}
    return render(request, 'filmwho/index.html', context)

def director_detail(request):
    return render(request, 'filmwho/director_detail.html', context=None)

def movies(request):
    return render(request, 'filmwho/movies/html', context=None)

def movie_detail(request):
    return render(request, 'filmwho/movie.detail.html', context=None)
