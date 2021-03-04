import requests
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import City

# Home view
def home(request):
    # API URL provided by OpenWeather.org
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=redacted"

    # get all City objects from the database table
    cities = City.objects.all()

    # initiate an empty list for all weather data of all the cities
    # Will be sent to the web page later
    weather_data = []

    # Iterate on the QuerySet of cities with contain all the city objects
    for city in cities:
        try:
            # Call the API URL on each city and convert the response to a json object
            r = requests.get(url.format(city)).json()

            # Select wanted data from the json object and store them into a dictionary
            weather = {
                'id': city.id,  # city's id in database
                'city': r['name'],
                'temperature': r['main']['temp'],
                'temp_min': r['main']['temp_min'],  # Min temperature
                'temp_max': r['main']['temp_max'],  # Max temperature
                'description': r['weather'][0]['description'].capitalize(),
                'icon': r['weather'][0]['icon']
            }

            # Append the dictionary containing selected data to the previous list
            weather_data.append(weather)

        # Invalid city input(eg. '1', 'A', 'a') will result in KeyError
        # And will be deleted from the QuerySet and generate a warning message on the web page
        except KeyError as e:
            deleteCity(request, city.id)
            messages.error(request, 'City Not Found')

    # Render the data object to the HTML web page
    context = {'weather_data': weather_data}
    return render(request, 'home.html', context)

# Add a new city by searching its name on the web page
def addCity(request):
    # Get user input from the form
    name = request.POST['city_name'].strip()
    # Create a City object from the city name input
    new_city = City(name=name)
    # To avoid City duplicates in the QuerySet
    if City.objects.filter(name=new_city).count() < 1:
        new_city.save()
    # Redirect to/Refresh Home
    return HttpResponseRedirect('/')

# Delete existing cities on the web page
def deleteCity(request, city_id):
    # Get which city to be deleted by its id
    city = City.objects.get(id=city_id)
    city.delete()
    # Redirect to/Refresh Home
    return HttpResponseRedirect('/')