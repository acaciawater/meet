'''
Created on Nov 30, 2016

@author: theo
'''
from models import Meting, Sensor, UserProfileData
from django.contrib.auth.models import User
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authorization import DjangoAuthorization, Authorization
from tastypie import fields
from tastypie.authentication import BasicAuthentication


class OpenGETAuthentication(BasicAuthentication):
    def is_authenticated(self, request, **kwargs):
        if request.method == 'GET':
            return True
        return BasicAuthentication.is_authenticated(self, request, **kwargs)
    
class UserResource(ModelResource):
#     sensors = fields.ToManyField('meet.api.SensorResource', 'sensor_resource')
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        fields = ['username', 'first_name', 'last_name', 'last_login', 'sensors']
        allowed_methods = ['get', 'post', 'put', 'patch']
        authentication = BasicAuthentication(realm='Acacia Meet')
        authorization = DjangoAuthorization()


class SensorResource(ModelResource):
    user = fields.ForeignKey(UserResource,'user')
    class Meta:
        queryset = Sensor.objects.all()
        resource_name = 'sensor'
        authentication = BasicAuthentication(realm='Acacia Meet')
        authorization = DjangoAuthorization()
        filtering = {'sensor_id':ALL}
        allowed_methods = ['get', 'post', 'put', 'patch']
        
        
class MetingResource(ModelResource):
    #user = fields.ForeignKey(UserResource,'user')
    sensor_pk= fields.ForeignKey(SensorResource, 'sensor_pk')
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
        allowed_methods = ['get', 'post', 'put', 'patch']
class UserProfileDataResource(ModelResource):
    user = fields.ForeignKey(UserResource,'user')
    class Meta:
        queryset = UserProfileData.objects.all()
        resource_name = 'userprofiledata'
        authentication = BasicAuthentication(realm='Acacia Meet')
        authorization = DjangoAuthorization()
        allowed_methods = ['get', 'post', 'put', 'patch']