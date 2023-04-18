from django.shortcuts import render
from django.views import View

from resume.models import Resume
from user.models import User


class Home(View):
    def get(self, request, *args, **kwargs):
        context = {}
        users = User.objects.all()
        context['users'] = users
        resumes = Resume.objects.all()
        context['resumes'] = resumes
        return render(request, 'index.html', context)
