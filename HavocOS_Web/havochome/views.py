from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {'author': 'Arna',
    'title': 'Blog Post 1',
    'content': 'First Post Content'
    },

    {'author': 'Arna',
    'title': 'Blog Post 2',
    'content': 'Second Post Content'
    }
]

def home(request):
    context = {
        'posts': posts
    }

    return render(request, 'havochome/home.html', context)

def about(request):
    return render(request, 'havochome/about.html',{'title': 'About'})


def downloads(request):
    return render(request, 'havochome/downloads.html')