from django.urls import path
from users import views

app_name = 'users'
urlpatterns = [
    path('user/', views.UserListCreateView.as_view(), name='user-list'),
    path('user/<int:pk>', views.UserDetailView.as_view(),
         name='user-detail'),
]
