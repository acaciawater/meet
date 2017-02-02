'''
Created on Nov 30, 2016

@author: theo
'''
from django.conf.urls import url, include
from api import MetingResource, UserResource, SensorResource, UserProfileDataResource
from django.contrib import admin
from tastypie.api import Api
from views import home
from . import views
from django.conf.urls.static import static
from django.conf import settings

v1 = Api(api_name='v1')
v1.register(MetingResource())
v1.register(UserResource())
v1.register(SensorResource())
v1.register(UserProfileDataResource())

urlpatterns = [
    url(r'^$', home),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1.urls)),
    url(r'^getusers/', views.getusers),
    url(r'^getpoints/', views.getpoints),
    url(r'^getseries/', views.getseries),

    ] +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



