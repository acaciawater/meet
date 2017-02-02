from django.core import serializers
from django.http.response import HttpResponse
from django.shortcuts import render
from django.conf import settings
from pip._vendor import requests
from models import Meting, User, Meetpunt
import json
from django.db.models import Q
import datetime as dt

def epoch_to_datetime(seconds):
    return dt.datetime.utcfromtimestamp(seconds).strftime("%Y-%m-%d %H:%M:%S.%f%Z")

def count_measurements(user):
    return Meting.objects.filter(sensor_pk__user__id=int(user.id)).count()

def count_measurement_points(user):
    return Meetpunt.objects.filter(meting__sensor_pk__user__id=int(user.id)).distinct().count()

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

def getseries(request):
    req = request.GET.urlencode()
    thumbnail_urls = {}

    start = request.GET.get('start')
    end = request.GET.get('end')
    user = request.GET.get('user')
     
    if start:
        start = epoch_to_datetime(float(start)/1000)
                
    if end:
        end = epoch_to_datetime(float(end)/1000)
                   
    if start!=None and user==None:
        # all points time-filtererd
        mps = Meetpunt.objects.exclude(Q(end__lte=start)|Q(start__gte=end))
    elif start==None and user!=None:
        # all points of user
        mps = Meetpunt.objects.filter(meting__sensor_pk__user__id=user)
    elif start!=None and user!=None:
        # user points filtered
        mps = Meetpunt.objects.filter(meting__sensor_pk__user__id=3).exclude(Q(end__lte=start)|Q(start__gte=end))
    else:
        # all points         
        mps = Meetpunt.objects.all()
    measurements = serializers.serialize('json',mps.distinct())
    
    for mp in mps:
        url = mp.thumbnail.url
        meting = mp.meting_set.all()[0]
        entity = meting.entity
        unit = meting.unit
        thumbnail_urls[mp.id] = {'url': url, 'entity':entity, 'unit':unit} 
    thumbnail_urls = json.dumps(thumbnail_urls)

    result = '['+measurements+','+thumbnail_urls+']'     
    return HttpResponse(result, content_type='application/json')
    

def getusers(request):
    req = request.GET.urlencode()
    if not req: 
        users = User.objects.all()
    if req:
        if req.split('=')[1] == 'with_measurements':
            users = User.objects.filter(sensor__meting__isnull=False).distinct()
    
    nr_of_series = {}
    for u in users:
        l = count_measurement_points(u)
        nr_of_series[u.username] = l
    nr_of_series_json = json.dumps(nr_of_series)
    users_json = serializers.serialize('json', users)
    
    result = '['+users_json+','+nr_of_series_json+']'
    
    return HttpResponse(result, content_type='application/json')
    
# def getthumbnail(request):
#     req = request.GET.urlencode()
#     req = request.path.split('<')[0]
    
    