import time
from datetime import datetime
from uuid import uuid4

from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


def today_at_ten_pm():
    current_time = timezone.now()
    today_ten_pm = (current_time.year, current_time.month,
                    current_time.day, 22, 0, 0, 0, 0, 0)
    seconds = time.mktime(today_ten_pm)
    return datetime.fromtimestamp(seconds)


class Event(models.Model):
    BUILDING_CHOICES = (
        ('AH', 'AH - Ana Mercedez Enriquez'),
        ('PB', 'PB - Pedro Bono'),
        ('GC', 'GC - Osvaldo Garcia de la Concha'),
        ('DP', 'DP - Ramon Picazo'),
        ('FD', 'FD - Fernando Defilo'),
        ('AJ', 'AJ - Arturo Jimenez Sabater'),
        ('PB', 'PB - Pedro Francisco Bono'),
        ('EP', 'EP - Ercilia Pepin'),
        ('Plazoleta', 'Plazoleta'),
        ('Bosquecito', 'Bosquecito'),
    )

    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    building = models.CharField(max_length=60, choices=BUILDING_CHOICES)
    description = models.CharField(max_length=500)
    start = models.DateTimeField(default=timezone.now, blank=True)
    # No event will last after 10PM (or it's very, very unlikely)
    end = models.DateTimeField(default=today_at_ten_pm, blank=True)

    def __str__(self):
        return f'{self.building} | {self.title}'


def image_path_with_uuid(instance, filename):
    return f'{instance.event_id}/{uuid4()}'


class EventImage(models.Model):
    image = models.ImageField(upload_to=image_path_with_uuid)
    event = models.ForeignKey(
        'Event', related_name='images', on_delete=models.CASCADE)
    uploaded = models.DateTimeField(auto_now_add=True)
