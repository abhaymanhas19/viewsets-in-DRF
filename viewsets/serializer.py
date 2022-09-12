from .models import songs
from rest_framework import serializers

class songserializer(serializers.ModelSerializer):
    class Meta:
        model=songs
        fields='__all__'