from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("federations.urls")),
    path('', include("teams.urls")),
    path('', include("players.urls")),
    path("", include("home.urls")),
    path('', include("registracion.urls")),
<<<<<<< HEAD
    path('accounts/',include('django.contrib.auth.urls')),
=======
>>>>>>> 0dba04d436131733b5081eafe74e04fe290d9c9d
        ]

if settings.DEBUG:
     from django.conf.urls.static import static
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)