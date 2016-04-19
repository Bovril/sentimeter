from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .classify import NB

def index(request):
    nb = NB()

    return HttpResponse(nb.classify_tweet("hello world"))


