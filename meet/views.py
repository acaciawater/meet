from django.shortcuts import render
from django.conf import settings
from models import Meting
import json

# Create your views here.
def home(request):
    pts = [{'id':m.pk,'lat':m.latitude,'lon': m.longitude} for m in Meting.objects.all()]
    return render(request, 'home.html', context = {'content': json.dumps(pts), 'api_key': settings.GOOGLE_MAPS_API_KEY})