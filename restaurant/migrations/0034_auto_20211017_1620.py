# Generated by Django 3.2.8 on 2021-10-17 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0033_auto_20211017_1537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='avail_tables',
        ),
        migrations.AddField(
            model_name='booking',
            name='avail_tables',
            field=models.IntegerField(default=1),
        ),
    ]