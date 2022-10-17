from django.urls import path

from measurement.views import ListCreateSensor, RetrieveUpdateSensor, CreateMeasurement

urlpatterns = [
    path('sensors/', ListCreateSensor.as_view()),
    path('sensors/<pk>/', RetrieveUpdateSensor.as_view()),
    path('measurements/', CreateMeasurement.as_view())
]
