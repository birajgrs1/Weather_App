from django.shortcuts import render
from django.contrib import messages
import requests 
import datetime

def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Pokhara'
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=8931b0c0d21be6f008582f8d51a87be1'
    params = {'units': 'metric'} 
    
    try:
        data = requests.get(url, params=params).json()  
        
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        
        day = str(datetime.date.today())  
        
        return render(request, 'index.html', {'description': description, 'icon': icon, 'temp': temp, 'day': day, 'city': city, 'exception_occurred': False})
    
    except Exception as e:
        exception_occurred = True
        messages.error(request, 'Entered data is not available or shown to API')
        day = datetime.date.today()
        
        return render(request, 'index.html', {'description': 'Clear sky', 'icon': '01d', 'temp': 20, 'day': day, 'city': 'Kathmandu', 'exception_occurred': exception_occurred})
