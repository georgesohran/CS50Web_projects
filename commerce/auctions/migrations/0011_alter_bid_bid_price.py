# Generated by Django 5.0.1 on 2024-01-25 15:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0010_alter_auction_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bid",
            name="bid_price",
            field=models.FloatField(),
        ),
    ]