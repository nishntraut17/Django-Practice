# myapp/views.py
from django.shortcuts import render
from .models import MyModel

from django.http import HttpResponse


def home(request):
    return HttpResponse("Hey I am a Django Server")


def success_page(request):
    return HttpResponse("This is a success page")
