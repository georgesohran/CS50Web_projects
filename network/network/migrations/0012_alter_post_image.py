# Generated by Django 5.0.2 on 2024-03-03 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0011_alter_user_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]