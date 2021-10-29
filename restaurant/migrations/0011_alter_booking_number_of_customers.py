# Generated by Django 3.2.8 on 2021-10-29 10:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0010_auto_20211028_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='number_of_customers',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]