from django.shortcuts import render
from django.views import View
from django.urls import resolve
from django.shortcuts import render, redirect
import pickle
import requests
from pprint import pprint
# Create your views here.
class basic_view(View):
    def get(self, request, *args, **kwargs):
        l=[1,2,3]
        return render(
            request,
            template_name="detect.html",context={'l':l}
        )
class detect_view(View):
    def get(self, request, *args, **kwargs):
        file = open('real_output.pkl', 'rb')
        data = pickle.load(file)
        values = [abs(x['depth']) for x in data]
        print(values)
        return render(
            request,
            template_name="maindetect.html",context={'value':values}
        )
class weather_view(View):
    def get(self, request, *args, **kwargs):
        url = 'https://samples.openweathermap.org/data/2.5/forecast/daily?zip=94040&appid=b6907d289e10d714a6e88b30761fae22'
        res = requests.get(url)
        data = res.json()
        l=[]
        h=[]
        m=[]
        for i in range(7):
            wind_speed = data['list'][i]['speed']
            print(wind_speed)
            if(wind_speed>4):
                h.append(wind_speed)
            elif(wind_speed>=2.53):
                m.append(wind_speed)
            else:
                l.append(wind_speed)

        return render(request,template_name='weathertemp.html',context={'high':h,'med':m,'low':l})