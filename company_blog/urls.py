from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_site.urls')),
    path('user/', include('my_user.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
