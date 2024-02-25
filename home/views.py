from django.http import HttpResponse
from django.shortcuts import render

from datetime import datetime

import requests
import json
# Create your views here.


def home(request):

    current_year = datetime.now().year

    return render(request, 'home/index.html', context={'current_year': current_year})


def projects(request):
    return HttpResponse('projects page')


def contact(request):
    return HttpResponse('contact page')


def runner(request):
    
    payload = {
        'key': 'c2fcd24120be45aabc3143744232608',
        'q': 'Makati',
    }

    response = requests.get('http://api.weatherapi.com/v1/current.json', params=payload)

    print(response.url)
    print(response.status_code)


    data = response.json()

    context = {
        'response': data
        
    }
 

    return render(request, 'home/test.html', context=context)
    