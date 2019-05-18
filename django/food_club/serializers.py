from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

from food_club.models import Event, EventImage


class EventImageSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="food_club:event-image-detail")
    image = Base64ImageField()
    event = serializers.HyperlinkedRelatedField(
        view_name='food_club:event-detail',
        queryset=Event.objects.all())

    class Meta:
        model = EventImage
        fields = ('url', 'image', 'event', 'uploaded')


class EventSerializer(serializers.HyperlinkedModelSerializer):
    images = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(
        view_name="food_club:event-detail")

    class Meta:
        model = Event
        fields = ('url', 'title', 'building',
                  'description', 'start', 'end', 'images',)

    # Only get the url paths of the images, I'm unsure if I should add
    # more info in the images array or just the url path to its image detail
    # view. Let me know what you think.
    def get_images(self, obj):
        request = self.context.get('request')
        id = getattr(obj, 'id')
        images = EventImage.objects.all().filter(event__id=id)
        serializer = EventImageSerializer(
            images, many=True, context={'request': request})
        return [data['image'] for data in serializer.data]
