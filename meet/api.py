'''
Created on Nov 30, 2016

@author: theo
'''
from models import Meting
from django.contrib.auth.models import User
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.authentication import Authentication

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        fields = ['username', 'first_name', 'last_name', 'last_login']
        authentication = Authentication()
        authorization = Authorization()
    
class MetingResource(ModelResource):
    #user = fields.ForeignKey(UserResource,'user')
    class Meta:
        queryset = Meting.objects.all()
        resource_name = 'meting'
        authentication = Authentication()
        authorization = Authorization()
        