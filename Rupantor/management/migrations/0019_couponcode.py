# Generated by Django 5.0.2 on 2024-06-12 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0018_alter_shippeditems_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='CouponCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('discountPercent', models.IntegerField(blank=True, help_text='Enter the percentage amount you are willing to provide', null=True)),
                ('discountAmount', models.IntegerField(blank=True, help_text='Enter the discount amount you are willing to provide', null=True)),
            ],
        ),
    ]