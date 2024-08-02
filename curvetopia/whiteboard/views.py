# whiteboard/views.py
from rest_framework.response import Response
from rest_framework import status,viewsets
from .models import Polyline
from .serializers import PolylineSerializer
from .processing import process_polylines
import json

class PolylineViewSet(viewsets.ModelViewSet):
    queryset = Polyline.objects.all()
    serializer_class = PolylineSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.get('data')
        polylines = json.loads(data)
        processed_polylines = process_polylines(polylines)
        return Response(processed_polylines, status=status.HTTP_201_CREATED)
