from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .views import Home

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', Home.as_view(), name="Home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('', include('user.urls'))
]

urlpatterns += [
    path('', include('resume.urls'))
]
