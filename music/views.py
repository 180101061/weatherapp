from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>hello friends<br><a href='https://www.google.com'>KOTKAR LODU</a></h1>")
