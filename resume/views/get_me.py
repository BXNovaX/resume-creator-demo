from django.shortcuts import render, redirect
from django.views import View

from resume.models import Resume


class GetMe(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            context = {}
            if request.user.resume:
                context['resume'] = request.user.resume
            return render(request, 'me.html', context)
        else:
            return render(request, '404.html', {})

    def post(self, request, *args, **kwargs):
        if request.user.resume:
            resume = request.user.resume
            resume.name = request.POST.get('name')
            resume.content = request.POST.get('content')
            resume.image_1 = request.FILES.get('image_1', resume.image_1)
            resume.image_2 = request.FILES.get('image_2', resume.image_2)
            resume.image_3 = request.FILES.get('image_3', resume.image_3)
            resume.save()
        else:
            name = request.POST.get('name')
            content = request.POST.get('content')
            image_1 = request.FILES.get('image_1')
            image_2 = request.FILES.get('image_2')
            image_3 = request.FILES.get('image_3')
            resume = Resume(name=name,
                            content=content,
                            image_1=image_1,
                            image_2=image_2,
                            image_3=image_3,
                            )
            resume.save()
            user = request.user
            user.resume = resume
            user.save()
        return redirect('Home')

