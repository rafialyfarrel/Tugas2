from django.shortcuts import render
from mywatchlist.models import Movies
from django.http import HttpResponse
from django.core import serializers

# Create your views here.z

def bonus(request):
    hasil = 0
    film = Movies.objects.all()
    for i in film:
        if i.watched == "Done":
            hasil += 1
    if hasil >= len(film) - hasil:
        return "Selamat, kamu sudah banyak menonton!"
    else :
        return "Wah, kamu masih sedikit menonton!" 

def show_Movies(request):
    data_Movies = Movies.objects.all()
    context = {
        'list_movies' : data_Movies,
        'nama' : 'Muhammad Rafialy Farrel',
        'id' : '2106751171',
        'giftcard' : bonus(request),
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = Movies.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Movies.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request,  id):
    data = Movies.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Movies.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")