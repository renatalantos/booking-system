# Generated by Django 3.2.8 on 2021-10-24 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0042_remove_booking_number_of_customers'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='Table',
        ),
    ]
