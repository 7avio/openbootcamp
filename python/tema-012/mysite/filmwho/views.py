from django.shortcuts import render, get_object_or_404
from .models import Director, Movie
from django.http import HttpResponse
from django.urls import resolve

class Tests:
    def current_url(request):
        match = resolve(request.path_info)
        return match.url_name

def index(request):
    directors = Director.objects.all()
    context = {
        'directors': directors,
        'url': Tests.current_url(request)
    }
    return render(request, 'filmwho/index.html', context)

def director_detail(request,director_id):
    director = get_object_or_404(Director, director_id=director_id)
    movies_rel = Director.objects.get(director_id=director_id).movie.all()
    context = {
        'director': director,
        'movies_rel': movies_rel,
        'url': Tests.current_url(request)
               }
    return render(request, 'filmwho/director_detail.html', context)

def movies(request):
    movies = Movie.objects.all().order_by('title')
    context = {
        'movies': movies,
        'url': Tests.current_url(request)}
    return render(request, 'filmwho/movies.html', context)

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, movie_id=movie_id)
    directors_rel = Movie.objects.get(movie_id=movie_id).directors.all()
    context = {
        'movie': movie,
        'directors_rel': directors_rel,
        'url': Tests.current_url(request)
    }
    return render(request, 'filmwho/movie_detail.html', context)
