'''
Created on Jan 13, 2017

@author: stephane
'''
from django.core.management.base import BaseCommand
from meet.models import Meetpunt
from django.db.models import Q


class Command(BaseCommand):
    help = "Assign a meetpunt for each meting that does not have one"
    
    def handle(self, *args, **options):
        meetpunt_without_start_or_end = Meetpunt.objects.filter(Q(start__isnull=True) | Q(end__isnull=True))
        for mp in meetpunt_without_start_or_end:
            mp.assignStartEnd()
            mp.save()
