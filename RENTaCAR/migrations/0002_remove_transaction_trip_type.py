# Generated by Django 3.1.7 on 2021-04-26 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RENTaCAR', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='trip_type',
        ),
    ]
