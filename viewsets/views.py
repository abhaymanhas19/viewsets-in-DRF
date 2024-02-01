from django.shortcuts import render

from .models import songs
from .serializer import songserializer

from rest_framework import viewsets

class studentcrudapi(viewsets.ModelViewSet):
    queryset=songs.objects.all()
    serializer_class=songserializer



### for usng viewst VIEWset CRuD operations
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing, creating, retrieving, updating, and deleting items.
    """

    def list(self, request):
        queryset = Item.objects.all()
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Item.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        item = get_object_or_404(Item.objects.all(), pk=pk)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        item = get_object_or_404(Item.objects.all(), pk=pk)
        serializer = ItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        item = get_object_or_404(Item.objects.all(), pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
