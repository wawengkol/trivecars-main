# Generated by Django 3.1.7 on 2021-04-28 05:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('RENTaCAR', '0007_auto_20210426_1450'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Transaction',
            new_name='Car_order',
        ),
    ]
