from rest_framework import generics
from food_club.models import Event, EventImage
from food_club.serializers import EventSerializer, EventImageSerializer


class EventListView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventDetailView(generics.RetrieveUpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventImageListView(generics.ListCreateAPIView):
    queryset = EventImage.objects.all()
    serializer_class = EventImageSerializer


class EventImageDetailView(generics.RetrieveUpdateAPIView):
    queryset = EventImage.objects.all()
    serializer_class = EventImageSerializer
