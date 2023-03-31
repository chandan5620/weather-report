from django.shortcuts import render
import json
import urllib.request


# Create your views here.
def index(request):
    if request.method == "POST":
        city = request.POST['city']
        res = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?q="+city+"&APPID=34dab784a5cb00f4e89228679d59d28c").read()
        json_data = json.loads(res)

        weather_data = {
            "country" : city.title,
            "country_code" : str(json_data['sys']['country']),
            "weather_info" : str(json_data['weather'][0]['main']),
            "temprature" : str(json_data['main']['temp'] ),
            "temp_min" : str(json_data['main']['temp_min']), 
            "temp_max" : str(json_data['main']['temp_max']),
            "pressure" : str(json_data['main']['pressure']),
            "humidity" : str(json_data['main']['humidity']),
        }               
        print(weather_data)
    else:
        weather_data={}
    return render(request, "index.html", {'data':weather_data})

#city = 'london'
#res = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?q="+city+"&APPID=34dab784a5cb00f4e89228679d59d28c").read()

#json_data1 = json.loads(res)


    