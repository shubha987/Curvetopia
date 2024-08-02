# whiteboard/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PolylineViewSet

router = DefaultRouter()
router.register(r'polylines', PolylineViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
