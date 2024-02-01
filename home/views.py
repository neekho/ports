from django.http import HttpResponse
from django.shortcuts import render

from datetime import datetime

# Create your views here.


def home(request):

    current_year = datetime.now().year

    return render(request, 'home/index.html', context={'current_year': current_year})


def projects(request):
    return HttpResponse('projects page')


def contact(request):
    return HttpResponse('contact page')