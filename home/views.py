from django.http import HttpResponse
from django.shortcuts import render

from datetime import datetime

import requests

from . forms import CityForm

# Create your views here.


def home(request):

    current_year = datetime.now().year

    return render(request, 'home/index.html', context={'current_year': current_year})


def projects(request):
    return HttpResponse('projects page')


def contact(request):
    return HttpResponse('contact page')



def get_weather(request, city_name):
    
    payload = {
        'key': 'c2fcd24120be45aabc3143744232608',
        'q': city_name,
    }
    
    response = requests.get('http://api.weatherapi.com/v1/current.json', params=payload)

    print(response.url)
    print(response.status_code)
    
    
    return response.json()
    


def runner(request):
    
    api_response = {}
    
    if request.method == 'POST':
        city_input = CityForm(request.POST)
        
        if city_input.is_valid():
            city_query = city_input.cleaned_data['city_input'].lower().split()
            print(city_query)
            
            api_response = get_weather(request, city_query)

            
    
    else:
        city_input = CityForm()
    
 


    context = {
        'city_input': city_input,
        'response': api_response
    }
 

    return render(request, 'home/test.html', context=context)
    