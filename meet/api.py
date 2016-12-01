'''
Created on Nov 30, 2016

@author: theo
'''
from models import Meting
from django.contrib.auth.models import User
from tastypie.resources import ModelResource
from tastypie.authorization import DjangoAuthorization
from tastypie import fields
from tastypie.authentication import BasicAuthentication

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        fields = ['username', 'first_name', 'last_name', 'last_login']
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()
    
class MetingResource(ModelResource):
    #user = fields.ForeignKey(UserResource,'user')
    class Meta:
        queryset = Meting.objects.all()
        resource_name = 'meting'
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()
        