from django.shortcuts import render, redirect
from django.views import View

from user.models import User


class ShowSingle(View):
    def get(self, request, usrname, *args, **kwargs):
        context = {}
        user = User.objects.get(username=usrname)
        if user.resume:
            context['resume'] = user.resume
        return render(request, 'show_single.html', context)
