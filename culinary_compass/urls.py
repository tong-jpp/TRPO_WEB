from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
     path('admin/', admin.site.urls),
    path('admipython manage.py runservern/', admin.site.urls),
    path('', include('recipes.urls')),
    path('users/', include('users.urls')),
    path('favorites/', include('favorites.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)