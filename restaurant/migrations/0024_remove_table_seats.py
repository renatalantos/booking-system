# Generated by Django 3.2.8 on 2021-10-16 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0023_alter_table_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='seats',
        ),
    ]
