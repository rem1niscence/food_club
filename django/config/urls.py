from django.contrib import admin
from django.urls import path, include
from users.models import ObtainAuthTokenAndUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', ObtainAuthTokenAndUser.as_view()),
    path('api/', include('food_club.urls')),
    path('api/', include('users.urls')),

]
