from django.db import models

class Wears(models.Model):
    pass

class Cart(models.Model):
    pass

class CustomerMessage(models.Model):
    msgId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=20)
    msg = models.TextField()
