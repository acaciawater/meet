'''
Created on Jan 6, 2017

@author: stephane
'''

from django.core.management.base import BaseCommand, CommandError
from meet.models import Meting


class Command(BaseCommand):
    help = "Assign a meetpunt for each meting that does not have one"
    
    def handle(self, *args, **options):
        metingen_without_meetpunt = Meting.objects.filter(meetpunt__isnull=True)
        for m in metingen_without_meetpunt:
            m.assignMeetpunt()
#     
#         print 'bla'