from django.shortcuts import render
from django.views import View

from resume.models import Resume


class Home(View):
    def get(self, request, *args, **kwargs):
        context = {}
        resumes = Resume.objects.all()
        context['resumes'] = resumes
        return render(request, 'index.html', context)
