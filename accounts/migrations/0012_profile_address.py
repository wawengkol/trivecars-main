# Generated by Django 3.1.7 on 2021-04-23 20:06

import address.models
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0003_auto_20200830_1851'),
        ('accounts', '0011_auto_20210423_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=address.models.AddressField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='address.address'),
        ),
    ]
