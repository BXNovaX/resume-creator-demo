from django.contrib.auth.models import AbstractUser
from django.db import models

from resume.models import Resume


class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/avatar/', blank=True)
    resume = models.ForeignKey(Resume, blank=True, null=True, on_delete=models.CASCADE, related_name='user')

    # def save(self):
    #     resume = Resume()
    #     resume.save()
    #     self.resume = resume
    #     return super(User, self).save()
