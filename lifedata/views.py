#from django.shortcuts import render

from rest_framework import generics

from . import models
from . import serializers

class ListCreateSleep(generics.ListCreateAPIView):
	queryset = models.Sleep.objects.all()
	serializer_class = serializers.SleepSerializer

class RetrieveUpdateDestroySleep(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Sleep.objects.all()
	serializer_class = serializers.SleepSerializer