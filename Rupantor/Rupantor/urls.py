from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from register import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', v.register, name='register'),
    path('', include('management.urls')),
    path('', include('django.contrib.auth.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)