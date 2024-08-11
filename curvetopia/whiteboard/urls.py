# whiteboard/urls.py
from django.urls import path
from .views import process_drawing

urlpatterns = [
    path('process-drawing/', process_drawing, name='process_drawing'),
]