# Generated by Django 4.0.3 on 2022-05-19 14:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0012_rename_cart_my_orders'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='My_Orders',
            new_name='My_Order',
        ),
    ]
