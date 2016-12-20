from django.contrib import admin
from models import Meting, Sensor
from django.contrib.admin.options import ModelAdmin

class MetingAdmin(admin.ModelAdmin):
    list_display = ('pk','sensor','date','entity','value','unit')
    list_filter = ('entity','date','sensor')
    
class SensorAdmin(admin.ModelAdmin):
    list_display = ('pk','sensor_id','sensor_type','assigned','user_id')
    list_filter = ('sensor_id','sensor_type','assigned','user_id')
    
# Register your models here.
admin.site.register(Meting,MetingAdmin)
admin.site.register(Sensor, SensorAdmin)