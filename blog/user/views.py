from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def login(request):
    return HttpResponse("Hola estas en el login")

def register(request):
    return HttpResponse("Hola estas en el register")
