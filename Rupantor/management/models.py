from django.db import models

class Wears(models.Model):
    categoryChoice = [
        ('SummerWear', 'Summerwear'),
        ('WinterWear', 'Winterwear')
    ]
    productId = models.AutoField(primary_key=True)
    category = models.CharField(max_length=20, choices=categoryChoice)
    productName = models.CharField(max_length=100)
    productColor = models.CharField(max_length=50, null=True)
    productBody = models.CharField(max_length=30, null=True)
    frontLength = models.CharField(max_length=30, null=True)
    backLength = models.CharField(max_length=30, null=True)
    productPrice = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.IntegerField()
    description = models.TextField()
    productImage = models.ImageField(blank=True)

    def __str__(self):
        return f"{self.productName} - {self.category}"

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

    def __str__(self):
        return f"{self.name} - {self.subject}"

class Featured(models.Model):
    message = models.CharField(max_length=50, default='Featured')
    product = models.ForeignKey(Wears, related_name='featured', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.message}"

class Offer(models.Model):
    Discount = models.CharField(max_length=50, default='Discounts')
    product = models.ForeignKey(Wears, related_name='discounted', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Discounts: {self.Discount} - {self.product}"