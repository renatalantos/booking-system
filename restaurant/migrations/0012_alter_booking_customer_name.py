# Generated by Django 3.2.8 on 2021-10-29 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0011_alter_booking_number_of_customers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='customer_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
