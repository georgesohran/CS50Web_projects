# Generated by Django 5.0.2 on 2024-03-06 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0014_remove_post_dislikes"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="dislikes",
        ),
    ]