from django.urls import path
from food_club import views

app_name = 'food_club'

urlpatterns = [
    path('events/', views.EventListView.as_view(), name='event_list'),
    path('events/<int:pk>/', views.EventDetailView.as_view(),
         name='event_detail'),
]
