from django.http import HttpResponse
from django.shortcuts import render
import os

def index(request):
    f = open("./GoogleHomeSpeak/audio.mp3","rb")
    response = HttpResponse()
    response.write(f.read())
    response['Content-Type'] = 'audio/mp3'
    return response
