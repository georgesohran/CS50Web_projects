# Generated by Django 5.0.1 on 2024-01-20 15:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0005_wathclist"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="WathcList",
            new_name="Watchlist",
        ),
    ]
