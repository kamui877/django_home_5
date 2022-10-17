from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя датчика')
    description = models.CharField(max_length=50, verbose_name='Информация о датчике')


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField(verbose_name='Температура')
    created_at = models.DateField(auto_now=True, verbose_name='Время замеров')
