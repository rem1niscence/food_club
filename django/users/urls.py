from django.urls import path
from users import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'users'
urlpatterns = [
    path('user/', views.UserListCreateView.as_view(), name='user-list'),
    path('token-auth/', obtain_auth_token, name='api-token-auth')
]
