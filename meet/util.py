'''
Created on Dec 9, 2016

@author: theo
'''
import requests
from django.conf import settings

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

