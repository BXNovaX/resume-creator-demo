# Generated by Django 4.2 on 2023-04-18 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resume", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="resume",
            name="image_1",
            field=models.ImageField(blank=True, upload_to="uploads/resume/"),
        ),
        migrations.AlterField(
            model_name="resume",
            name="image_2",
            field=models.ImageField(blank=True, upload_to="uploads/resume/"),
        ),
        migrations.AlterField(
            model_name="resume",
            name="image_3",
            field=models.ImageField(blank=True, upload_to="uploads/resume/"),
        ),
    ]