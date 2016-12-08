'''
Created on Nov 30, 2016

@author: theo
'''
from models import Meting
from django.contrib.auth.models import User
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authorization import DjangoAuthorization
from tastypie import fields
from tastypie.authentication import BasicAuthentication

class OpenGETAuthentication(BasicAuthentication):
    def is_authenticated(self, request, **kwargs):
        if request.method == 'GET':
            return True
        return BasicAuthentication.is_authenticated(self, request, **kwargs)
    
class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        fields = ['username', 'first_name', 'last_name', 'last_login']
        authentication = BasicAuthentication(realm='Acacia Meet')
        authorization = DjangoAuthorization()
    
class MetingResource(ModelResource):
    #user = fields.ForeignKey(UserResource,'user')
    class Meta:
        queryset = Meting.objects.all()
        resource_name = 'meting'
        authentication = BasicAuthentication(realm='Acacia Meet')
        authorization = DjangoAuthorization()
        filtering = {
            'entity': ALL,
            'date': ALL,
            'sensor': ALL
            }
        