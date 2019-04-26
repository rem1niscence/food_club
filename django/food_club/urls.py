from django.urls import path
from food_club import views

app_name = 'food_club'

urlpatterns = [
    path('event/', views.EventListView.as_view(), name='event-list'),
    path('event /<int:pk>/', views.EventDetailView.as_view(),
         name='event-detail'),
    path('eventimage/', views.EventImageListView.as_view(),
         name='event-image-list'),
    path('eventimage/<int:pk>', views.EventImageDetailView.as_view(),
         name='event-image-detail'),
]
