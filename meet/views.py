from django.core import serializers
from django.http.response import HttpResponse
from django.shortcuts import render
from django.conf import settings
from pip._vendor import requests
from models import Meting, User
import json

def count_measurements(user):
    return Meting.objects.filter(sensor_pk__user__id=int(user.id)).count()

def home(request):
    return render(request, 'home.html', context = {'api_key': settings.GOOGLE_MAPS_API_KEY})

# User.objects.all() / u.sensor_Set.all()
def getpoints(request):
    req = request.GET.urlencode()
    if req: 
        user_id = req.split('=')[1]
        m = Meting.objects.filter(sensor_pk__user__id=user_id)
        measurements = serializers.serialize('json',m)
    if not req:
        m = Meting.objects.all()
        measurements = serializers.serialize('json',m.distinct())
    return HttpResponse(measurements, content_type='application/json')

def getusers(request):
    req = request.GET.urlencode()
    if not req: 
        users = User.objects.all()
    if req:
        if req.split('=')[1] == 'with_measurements':
            users = User.objects.filter(sensor__meting__isnull=False).distinct()
    
    nr_of_measurements = {}
    for u in users:
        l = count_measurements(u)
        nr_of_measurements[u.username] = l
    nr_of_measurements_json = json.dumps(nr_of_measurements)
    users_json = serializers.serialize('json', users)
    
    result = '['+users_json+','+nr_of_measurements_json+']'
    
    return HttpResponse(result, content_type='application/json')
    
    
    