from django.urls import path
from . import views

app_name = 'filmwho'
urlpatterns = [
    path('', views.index, name='index'),
    path('director_detail/<int:director_id>/', views.director_detail, name='director_detail'),
    path('movies/', views.movies, name='movies'),
    path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail')
]