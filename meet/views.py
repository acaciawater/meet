from django.core import serializers
from django.http.response import HttpResponse
from django.shortcuts import render
from django.conf import settings
from pip._vendor import requests
from .models import Meting

def home(request):
    return render(request, 'home.html', context = {'api_key': settings.GOOGLE_MAPS_API_KEY})


def getpoints(request):
    sensor_id = request.GET.urlencode().split('=')[1]
    u = Meting.objects.filter(sensor=sensor_id)
    users = serializers.serialize('json',u.distinct())
    return HttpResponse(users, content_type='application/json')

def getusers(request):
    points = serializers.serialize('json',Meting.objects.all()) 
    return HttpResponse(points, content_type='application/json')
    
    
    