from django.shortcuts import render

from .models import songs
from .serializer import songserializer

from rest_framework import viewsets

class studentcrudapi(viewsets.ModelViewSet):
    queryset=songs.objects.all()
    serializer_class=songserializer