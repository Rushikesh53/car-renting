# Generated by Django 4.0.3 on 2022-04-19 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_date_my_order_renting_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='mileage',
            field=models.CharField(default=3, max_length=2),
            preserve_default=False,
        ),
    ]