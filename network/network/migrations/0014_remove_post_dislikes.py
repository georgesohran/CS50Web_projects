# Generated by Django 5.0.2 on 2024-03-05 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0013_user_about_me"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="dislikes",
        ),
    ]
