# Generated by Django 5.0.2 on 2024-04-29 10:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_remove_cart_productamount_remove_cart_productid_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together={('user', 'product')},
        ),
    ]
