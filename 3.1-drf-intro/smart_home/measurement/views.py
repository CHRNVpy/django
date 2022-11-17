# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all().order_by('id')
    serializer_class = SensorSerializer


class MeasurementView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

# Без этой функции не работает POST в Postman, sensor_id не принимает. Если ее убрать
# и добавить в MeasurementSerializer в Fields = ('sensor_id', ...) то все работает и в браузере
# и в Postman, но тогда в json ответе строка 'sensor_id' появляется соответственно. Как сделать лучше ?
    def perform_create(self, serializer):
        sensor = self.request.data.get('sensor_id')
        sensor_id = Sensor.objects.get(id=sensor)
        temperature = self.request.data.get('temperature')
        photo = self.request.data.get('photo')
        return serializer.save(sensor_id=sensor_id, temperature=temperature, photo=photo)



class SensorDetailView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
