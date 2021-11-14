from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50, null=True,
                            blank=True, verbose_name='Stadt Name')
    lon = models.FloatField(default=0, verbose_name='Longitude')
    lat = models.FloatField(default=0, verbose_name='Latitude')
