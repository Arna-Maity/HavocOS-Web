from django.shortcuts import render
from django.http import HttpResponse
from havochome.models import Developer, Device


def home(request):
    return render(request, 'havochome/home.html')

def about(request):
    return render(request, 'havochome/about.html',{'title': 'About'})


def downloads(request):
    return render(request, 'havochome/downloads.html', {'title': 'Downloads'})