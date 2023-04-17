from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login

from user.models import User


class SignUp(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'signup.html', {})

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            user = User(username=username, password=make_password(password))
            user.save()
            login(request, user)
            return redirect('GetMe')
        else:
            return render(request, 'signup.html', {'error': 'Password does not match!'})
