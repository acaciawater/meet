from django.contrib import admin
from models import Meting

class MetingAdmin(admin.ModelAdmin):
    list_display = ('pk','sensor','date','entity','value','unit')
    list_filter = ('entity','date','sensor')
    
# Register your models here.
admin.site.register(Meting,MetingAdmin)