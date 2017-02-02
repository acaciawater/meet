'''
Created on Dec 9, 2016

@author: theo
'''
import requests
from django.conf import settings
from django.utils.text import slugify
from math import sin, cos, sqrt, atan2, radians
import matplotlib.pylab as plt

# thumbnail size and resolution
THUMB_DPI=72
THUMB_SIZE=(9,3) # inch

class PostcodeException(Exception):
    def __init__(self,response):
        self.code = response.status_code
        self.error = response.json().get('error',None)

    def __str__(self):
        return self.error

def check_address(postcode,huisnummer):
    ''' check geldig adres '''
    response = requests.get(url='https://postcode-api.apiwise.nl/v2/addresses',
                            params={'postcode':postcode,'number': huisnummer},
                            headers={'X-Api-Key':settings.POSTCODE_API_KEY})
    # TODO: check toevoeging (letter)
    if response.status_code == 200:
        adrs = response.json()['_embedded']['addresses']
        return adrs
    else:
        raise PostcodeException(response)

def check_postcode(postcode):
    ''' check voor geldige postcode '''
    response = requests.get(url='https://postcode-api.apiwise.nl/v2/postcodes/'+postcode,
                            headers={'X-Api-Key':settings.POSTCODE_API_KEY})
    if response.status_code == 200:
        # OK
        return True
    elif response.status_code == 404:
        # Not found
        return False
    else:
        raise PostcodeException(response)

def distance(obj1, obj2):
    R = 6373.0
    lat1 = radians(obj1.latitude)
    lon1 = radians(obj1.longitude)
    lat2 = radians(obj2.latitude)
    lon2 = radians(obj2.longitude)
    dlon = lon2 - lon1
    dlat = lat2 - lat1    
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c * 1000
    
def is_in_range(obj1,obj2,meters):
    ''' check if two locations are within range'''
    return distance(obj1,obj2) <= meters

def thumbnail_upload(object, filename):
    return '/media/thumbnails/%s' % filename

def save_thumbnail(pandas_series,imagefile):
    plt.figure(figsize=THUMB_SIZE,dpi=THUMB_DPI)
    try:
        n = pandas_series.count() / (THUMB_SIZE[0]*THUMB_DPI)
        if n > 1:
            #use data thinning: take very nth row
            src = pandas_series.iloc[::n]
        else:
            src = pandas_series
        options = {'grid': False, 'legend': False}
        src.plot(**options)
        plt.savefig(imagefile,transparent=True)
    except:
        pass
    plt.close()