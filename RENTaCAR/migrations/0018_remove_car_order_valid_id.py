# Generated by Django 3.1.7 on 2021-05-05 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RENTaCAR', '0017_auto_20210504_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car_order',
            name='valid_id',
        ),
    ]
