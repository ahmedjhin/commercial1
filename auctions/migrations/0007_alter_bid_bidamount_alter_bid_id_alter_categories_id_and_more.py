# Generated by Django 4.2.5 on 2023-10-05 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_listing_created_at_listing_isactive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bidAmount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bid',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='categories',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='listing',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
