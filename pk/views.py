from django.db import models
from rest_framework import viewsets
from .models import Cricket
from django.http import HttpResponse

class CricketView():
    queryset = Cricket.objects.all()




