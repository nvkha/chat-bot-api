import sys
import os
os.chdir("..")
sys.path.append(os.getcwd())
from app.settings import OPENWEATHER_API
import requests
import json
from geopy.geocoders import Nominatim
from pathlib import Path

class WeatherSkills:
     
    __geolocator = Nominatim(user_agent="my_app")
    
    @classmethod
    def get_weather_forecast(cls, question):
        if "mai" in question:
            day_forecast = 0
        else:
            day_forecast = 1

        city = "Cà Mau"
        name_with_type = "tỉnh Cà Mau"

        d = Path(__file__).resolve().parents[1]
        with open(os.path.join(d, 'files/local.json'), encoding="utf-8") as f:
            local = json.load(f)
            for i in local:
                if local[i]["name"].lower() in question.lower():
                    city = local[i]["name"].lower()
                    name_with_type = local[i]["name_with_type"].lower()
                    break
                       
        location = cls.__geolocator.geocode(city)
        api_key = OPENWEATHER_API["key"]
        url = (f"https://api.openweathermap.org/data/2.5/onecall?" +
                f"lat={location.latitude}&lon={location.longitude}" +
                f"&exclude=hourly,minutely,current&appid={api_key}" +
                "&lang=vi&units=metric")    

       
        response = requests.get(url)
        forecast = response.json()
        weather = forecast['daily'][day_forecast]
        text = f"Nhiệt độ {weather['temp']['day']} độ và {weather['weather'][0]['description']} tại {name_with_type}"
        if "ngày mai" in question:
            text = f"Dự báo thời tiết ngày mai tại {name_with_type}, nhiệt độ {weather['temp']['day']} độ và {weather['weather'][0]['description']}"
            
        return text


