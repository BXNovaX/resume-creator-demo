from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login

from user.models import User


class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html', {})

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        raw_password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
            if check_password(raw_password, user.password):
                login(request, user)
                return redirect('Home')
        except:
            return render(request, 'login.html', {'error': 'Invalid username or password!'})
