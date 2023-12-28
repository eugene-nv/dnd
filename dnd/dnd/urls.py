from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from dnd import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('characters.urls')),
    path('arena/', include('arena.urls')),
    path('bestiary/', include('bestiary.urls')),

    path('users/', include('users.urls')),

    path('api/', include('api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)