# Generated by Django 3.2.8 on 2021-10-28 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0008_booking_created_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='created_on',
        ),
    ]
