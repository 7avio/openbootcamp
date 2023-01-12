from django.urls import path
from . import views

app_name = 'filmwho'
urlpatterns = [
    path('', views.index, name='index'),
]