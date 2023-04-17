from django.urls import path

from .views import *


urlpatterns = [
    path('me/', GetMe.as_view(), name='GetMe'),
    path('<str:usrname>/', ShowSingle.as_view(), name='ShowSingle'),
]
