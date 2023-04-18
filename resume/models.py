from ckeditor.fields import RichTextField
from django.db import models


class Resume(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    content = RichTextField(null=True, blank=True)
    image_1 = models.ImageField(upload_to='uploads/resume/', blank=True)
    image_2 = models.ImageField(upload_to='uploads/resume/', blank=True)
    image_3 = models.ImageField(upload_to='uploads/resume/', blank=True)
