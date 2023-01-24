from django.urls import path
from . import views

app_name = 'filmwho'
urlpatterns = [
    path('', views.index, name='index'),
    path('director_detail/', views.director_detail, name='director_detail'),
    path('movies/', views.movies, name='movies'),
]