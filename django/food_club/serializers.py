from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

from food_club.models import Event, EventImage


class EventSerializer(serializers.HyperlinkedModelSerializer):
    images = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='food_club:event-image-detail',
        queryset=EventImage.objects.all())

    class Meta:
        model = Event
        fields = ('id', 'title', 'building',
                  'description', 'start', 'end', 'images')


class EventImageSerializer(serializers.HyperlinkedModelSerializer):
    image = Base64ImageField()
    event = serializers.HyperlinkedRelatedField(
        view_name='food_club:event-detail',
        queryset=Event.objects.all())

    class Meta:
        model = EventImage
        fields = ('id', 'image', 'event', 'uploaded')
