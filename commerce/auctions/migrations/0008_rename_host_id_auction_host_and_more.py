# Generated by Django 5.0.1 on 2024-01-23 15:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0007_auction_current_price"),
    ]

    operations = [
        migrations.RenameField(
            model_name="auction",
            old_name="host_id",
            new_name="host",
        ),
        migrations.RenameField(
            model_name="bid",
            old_name="auction_id",
            new_name="auction",
        ),
        migrations.RenameField(
            model_name="bid",
            old_name="user_id",
            new_name="user",
        ),
        migrations.RenameField(
            model_name="comment",
            old_name="auction_id",
            new_name="auction",
        ),
        migrations.RenameField(
            model_name="comment",
            old_name="user_id",
            new_name="user",
        ),
        migrations.RenameField(
            model_name="watchlist",
            old_name="auction_id",
            new_name="auction",
        ),
        migrations.RenameField(
            model_name="watchlist",
            old_name="user_id",
            new_name="user",
        ),
        migrations.RemoveField(
            model_name="auction",
            name="current_price",
        ),
        migrations.AddField(
            model_name="bid",
            name="time",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 23, 15, 1, 0, 320791)
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="auction",
            name="time",
            field=models.DateTimeField(),
        ),
    ]
