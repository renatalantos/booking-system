# Generated by Django 3.2.8 on 2021-10-16 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0021_alter_table_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='category',
            field=models.CharField(choices=[('Seats2', 'Couple'), ('Sets4', 'Family of Four')], max_length=7),
        ),
    ]
