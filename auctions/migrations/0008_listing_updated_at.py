# Generated by Django 4.2.5 on 2023-10-05 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_alter_bid_bidamount_alter_bid_id_alter_categories_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
