# Generated by Django 4.2 on 2023-04-18 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_alter_user_resume"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(blank=True, upload_to="uploads/avatar/"),
        ),
    ]