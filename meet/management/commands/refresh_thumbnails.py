'''
Created on Jan 27, 2017

@author: stephane
'''
from django.core.management.base import BaseCommand
from meet.models import Meetpunt


class Command(BaseCommand):
    help = "Assign a meetpunt for each meting that does not have one"
    
    def handle(self, *args, **options):
        mps = Meetpunt.objects.all()
        for mp in mps:
            mp.make_thumbnail()
            mp.save()