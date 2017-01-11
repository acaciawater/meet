from django.contrib import admin
from models import Meting, Sensor, Meetpunt
from django.contrib.admin.options import ModelAdmin

class MetingAdmin(admin.ModelAdmin):
    list_display = ('pk','sensor','date','entity','value','unit','sensor_pk')
    list_filter = ('entity','date','sensor', 'sensor_pk')
    
class SensorAdmin(admin.ModelAdmin):
    list_display = ('pk','sensor_id','sensor_type','assigned','user_id')
    list_filter = ('sensor_id','sensor_type','assigned','user_id')

class MeetpuntAdmin(admin.ModelAdmin):
    list_display = ('pk', 'latitude', 'longitude')
    list_filter = ('latitude', 'longitude')

    
# Register your models here.
admin.site.register(Meting,MetingAdmin)
admin.site.register(Sensor, SensorAdmin)
admin.site.register(Meetpunt, MeetpuntAdmin)