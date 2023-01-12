from django.shortcuts import render
from .models import Director, Movie
from django.http import HttpResponse

#
def index(request):
    item = Director.objects.get(pk=1)
    context = {'item': item}
    return render(request, 'filmwho/index.html', context)

