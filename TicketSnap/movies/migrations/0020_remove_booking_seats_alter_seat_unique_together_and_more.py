# Generated by Django 5.0.2 on 2024-05-03 12:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0019_alter_seat_unique_together_seat_showtime_mapper_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='seats',
        ),
        migrations.AlterUniqueTogether(
            name='seat',
            unique_together={('row', 'number')},
        ),
        migrations.AddField(
            model_name='booking',
            name='is_booked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='seat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.seat'),
        ),
        migrations.RemoveField(
            model_name='seat',
            name='is_booked',
        ),
        migrations.RemoveField(
            model_name='seat',
            name='showtime_mapper',
        ),
    ]
