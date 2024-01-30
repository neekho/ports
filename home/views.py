from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.


def home(request):
    return render(request, 'home/index.html', context={})


def projects(request):
    return HttpResponse('projects page')


def contact(request):
    return HttpResponse('contact page')