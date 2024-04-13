# Generated by Django 5.0.2 on 2024-04-13 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productId', models.IntegerField()),
                ('productName', models.CharField(max_length=50)),
                ('productAmount', models.IntegerField()),
                ('productPrice', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CustomerMessage',
            fields=[
                ('msgId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=20)),
                ('msg', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Wears',
            fields=[
                ('productId', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(choices=[('SummerWear', 'Summerwear'), ('WinterWear', 'Winterwear')], max_length=20)),
                ('productName', models.CharField(max_length=50)),
                ('productColor', models.CharField(max_length=20)),
                ('productPrice', models.DecimalField(decimal_places=2, max_digits=8)),
                ('available', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]