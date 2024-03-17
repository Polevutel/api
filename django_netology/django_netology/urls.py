from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import SensorViewSet, TemperatureMeasurementViewSet

router = DefaultRouter()
router.register(r'sensors', SensorViewSet)
router.register(r'measurements', TemperatureMeasurementViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
