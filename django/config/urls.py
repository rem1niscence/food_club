from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

MEDIA_FILE_PATHS = static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('food_club.urls'))
] + MEDIA_FILE_PATHS
