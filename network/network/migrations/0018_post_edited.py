# Generated by Django 5.0.2 on 2024-03-09 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0017_rename_like_post_like_liked_post"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="edited",
            field=models.BooleanField(blank=True, default=False),
            preserve_default=False,
        ),
    ]
