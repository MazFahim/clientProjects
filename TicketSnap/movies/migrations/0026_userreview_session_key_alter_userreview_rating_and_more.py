# Generated by Django 5.0.2 on 2024-07-10 10:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0025_alter_couponcode_discountamount_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='userreview',
            name='session_key',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='userreview',
            name='rating',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userreview',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review', to=settings.AUTH_USER_MODEL),
        ),
    ]
