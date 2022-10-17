from rest_framework import generics, status
from rest_framework.response import Response
from measurement.models import Sensor
from measurement.serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer


class ListCreateSensor(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = SensorSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateMeasurement(generics.CreateAPIView):
    def create(self, request, *args, **kwargs):
        serializer = MeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RetrieveUpdateSensor(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = SensorSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

