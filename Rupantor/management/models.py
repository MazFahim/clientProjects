from django.db import models

class Wears(models.Model):
    categoryChoice = [
        ('SummerWear', 'Summerwear'),
        ('WinterWear', 'Winterwear')
    ]
    productId = models.AutoField(primary_key=True)
    category = models.CharField(max_length=20, choices=categoryChoice)
    productName = models.CharField(max_length=50)
    productColor = models.CharField(max_length=20)
    productBody = models.CharField(max_length=30)
    frontLength = models.IntegerField()
    backLength = models.IntegerField()
    productPrice = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.IntegerField()
    description = models.TextField()

class Cart(models.Model):
    productId = models.IntegerField()
    productName = models.CharField(max_length=50)
    productAmount = models.IntegerField()
    productPrice = models.IntegerField()

class CustomerMessage(models.Model):
    msgId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=20)
    msg = models.TextField()

class Featured(models.Model):
    pass

class Offer(models.Model):
    pass