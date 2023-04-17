from django.shortcuts import render, redirect
from django.views import View

from user.models import User


class ShowSingle(View):
    def get(self, request, usrname, *args, **kwargs):
        user = User.objects.get(username=usrname)
        return render(request, 'show_single.html', {"resume": user.resume})
