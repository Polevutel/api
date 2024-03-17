from rest_framework import viewsets
from rest_framework.response import Response
from .models import Sensor, TemperatureMeasurement
from .serializers import SensorSerializer, SensorDetailSerializer, TemperatureMeasurementSerializer

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def list(self, request):
        sensors = Sensor.objects.values('id', 'name', 'description')
        return Response(sensors)

    def retrieve(self, request, pk=None):
        sensor = self.get_object()
        serializer = SensorDetailSerializer(sensor)
        return Response(serializer.data)

class TemperatureMeasurementViewSet(viewsets.ModelViewSet):
    queryset = TemperatureMeasurement.objects.all()
    serializer_class = TemperatureMeasurementSerializer
