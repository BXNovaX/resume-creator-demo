from django.contrib import admin
from django.urls import path, include

from .views import Home

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', Home.as_view(), name="Home"),
]

urlpatterns += [
    path('', include('user.urls'))
]

urlpatterns += [
    path('', include('resume.urls'))
]
