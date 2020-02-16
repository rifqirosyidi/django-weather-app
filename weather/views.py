import requests
from django.shortcuts import render, redirect
from .models import CitiesWeather
from .forms import CityForm


# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&lang=id&appid=9f948804a745fb30917bb5d97ca56f99'

    cities = CitiesWeather.objects.all()

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    form = CityForm()

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()

        city_weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']
        }

        weather_data.append(city_weather)

    print(weather_data)

    context = {
        'weather_data': weather_data,
        'form': form
    }

    return render(request, 'weather/index.html', context)