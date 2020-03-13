from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Album


def index(request):
    all_albums = Album.objects.all()
    return render(request(request, "music/index.html", {'all_albums': all_albums}))


def detail(request, album_id):
    return HttpResponse("<h2>Details for album id:" + str(album_id) + "<h2>")


