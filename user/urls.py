from django.urls import path

from .views import *

urlpatterns = [
    path('login/', Login.as_view(), name="Login"),
    path('signup/', SignUp.as_view(), name="Signup"),
    path('logout/', LogOut.as_view(), name="LogOut"),
]