from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse
from .models import Art

# Create your views here.

def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')

def art_gallery(request):
    art = Art.objects.all()
    return render(request, 'art/index.html',
    {'art': art})

def art_detail(request):
    art = Art.objects.all()
    return render(request, 'art/detail.html', {'art': art})

# def collection(request):
#     return HttpResponse("works the art likes")
