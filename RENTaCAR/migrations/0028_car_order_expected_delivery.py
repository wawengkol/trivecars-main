# Generated by Django 3.1.7 on 2021-05-31 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RENTaCAR', '0027_auto_20210514_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='car_order',
            name='expected_delivery',
            field=models.DateTimeField(null=True),
        ),
    ]