# Generated by Django 3.1.7 on 2021-04-11 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='birthd_ate',
            new_name='birth_date',
        ),
        migrations.RenameField(
            model_name='registration',
            old_name='gender_female',
            new_name='gender',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='gender_male',
        ),
    ]