# Register your models here.
from django.contrib import admin

from measurement.models import Sensor, Measurement


admin.site.register(Sensor)
admin.site.register(Measurement)
