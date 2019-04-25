from rest_framework import serializers

from food_club.models import Event


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'building', 'description', 'start', 'end')
