import time
from datetime import datetime
from uuid import uuid4

from django.db import models
from django.utils import timezone


def today_at_ten_pm():
    current_time = timezone.now()
    today_ten_pm = (current_time.year, current_time.month,
                    current_time.day, 22, 0, 0, 0, 0, 0)
    seconds = time.mktime(today_ten_pm)
    return datetime.fromtimestamp(seconds)


class Event(models.Model):
    BUILDING_CHOICES = (
        (0, 'AH - Ana Mercedez Enriquez'),
        (1, 'PB - Pedro Bono'),
        (2, 'GC - Osvaldo Garcia de la Concha'),
        (3, 'DP - Ramon Picazo'),
        (4, 'FD - Fernando Defilo'),
        (5, 'AJ - Arturo Jimenez Sabater'),
        (6, 'PB - Pedro Francisco Bono'),
        (7, 'EP - Ercilia Pepin'),
        (8, 'Plazoleta'),
        (9, 'Bosquecito'),
    )

    title = models.CharField(max_length=150)
    building = models.SmallIntegerField(choices=BUILDING_CHOICES)
    description = models.CharField(max_length=500)
    start = models.DateTimeField(default=timezone.now, blank=True)
    # No event will last after 10PM (or it's very, very unlikely)
    end = models.DateTimeField(default=today_at_ten_pm, blank=True)

    def __str__(self):
        return f'{self.BUILDING_CHOICES[self.building][1]} | {self.title}'


def image_path_with_uuid(instance, filename):
    return f'{instance.event_id}/{uuid4()}'


class EventImage(models.Model):
    image = models.ImageField(upload_to=image_path_with_uuid)
    event = models.ForeignKey(
        'Event', related_name='images', on_delete=models.CASCADE)
    uploaded = models.DateTimeField(auto_now_add=True)
