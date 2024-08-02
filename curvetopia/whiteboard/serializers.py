# whiteboard/serializers.py
from rest_framework import serializers
from .models import Polyline

class PolylineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polyline
        fields = '__all__'
