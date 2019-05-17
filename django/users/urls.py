from django.urls import path
from users import views

app_name = 'users'
urlpatterns = [
    path('user/', views.UserListCreateView.as_view(), name='user-list')
]
