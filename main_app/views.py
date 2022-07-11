from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("hey")

def profile(request):
    return HttpResponse("artist info here")

def my_gallery(request):
    return HttpResponse("artists works display")

def collection(request):
    return HttpResponse("works the art likes")
