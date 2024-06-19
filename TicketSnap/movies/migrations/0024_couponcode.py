# Generated by Django 5.0.2 on 2024-06-03 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0023_booking_session_key_alter_booking_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='CouponCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('discountPercent', models.IntegerField(help_text='Enter the discount amount you are willing to provide', null=True)),
                ('discountAmount', models.IntegerField(help_text='Enter the discount amount you are willing to provide', null=True)),
            ],
        ),
    ]