# Generated by Django 3.2.8 on 2021-10-16 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='category',
            field=models.CharField(choices=[('Inside', 'Inside'), ('Outside', 'Outside')], max_length=7),
        ),
    ]