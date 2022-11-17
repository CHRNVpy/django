from django.db import models



# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)


    def __str__(self):
        return f'{self.name}: {self.description}'


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(null=True, blank=True, upload_to='photo')

    def __str__(self):
        return f'{self.sensor_id.name}: Показания на {self.created_at}'
