# Generated by Django 5.0.2 on 2024-07-14 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0024_remove_wears_categories_remove_wears_summerorwinter_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreview',
            name='message',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='userreview',
            name='rating',
            field=models.IntegerField(null=True),
        ),
    ]