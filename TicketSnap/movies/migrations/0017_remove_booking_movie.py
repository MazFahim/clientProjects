# Generated by Django 5.0.2 on 2024-04-29 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0016_showtimemapper_booking_bookingtime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='movie',
        ),
    ]
