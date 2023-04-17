from django.shortcuts import redirect
from django.views import View
from django.contrib.auth import logout


class LogOut(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('Home')
