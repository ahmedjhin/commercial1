# Generated by Django 4.1.7 on 2023-11-12 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_closedactions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='closedactions',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
