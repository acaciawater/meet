'''
Created on Nov 30, 2016

@author: theo
'''
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=bf2dkr41@s4agtbbwlw5*n&uufa58q+i7n^!p+8ee9#%v@a=6'

DATABASES = {
    'default': {
    'ENGINE': 'django.contrib.gis.db.backends.postgis',
    'NAME': 'meet',
    },
}
