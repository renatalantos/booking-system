# Generated by Django 3.2.8 on 2021-10-16 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0024_remove_table_seats'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
        migrations.DeleteModel(
            name='Table',
        ),
    ]
