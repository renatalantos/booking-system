# Generated by Django 3.2.8 on 2021-10-16 17:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurant', '0015_auto_20211016_1717'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_category', models.CharField(choices=[('A la carte', 'A la carta'), ('House special', 'Special'), ('Vegetarian', 'Vegetarian'), ('Vegan', 'Vegan')], max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Inside', 'Inside'), ('Outside', 'Outside')], max_length=7)),
                ('table_number', models.IntegerField()),
                ('seats', models.IntegerField(default=2)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('number_of_customers', models.IntegerField()),
                ('number_of_tables', models.IntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu', to='restaurant.menu')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reserved_table', to='restaurant.table')),
            ],
        ),
    ]
