# Generated by Django 4.0.3 on 2022-05-19 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_cart_renting_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='renting_date',
        ),
    ]
