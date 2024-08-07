from django.db import models
from django.conf import settings
from django.utils import timezone


class Wears(models.Model):
    CATEGORY_CHOICES = [
        ('SummerWear', 'Summerwear'),
        ('WinterWear', 'Winterwear'),
        ('Western', 'Western'),
        ('Cotton', 'Cotton')
    ]
    productId = models.AutoField(primary_key=True)
    categories = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='SummerWear')
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
        return f"{self.productName} - {self.categories}"



class Cart(models.Model):
    product = models.ForeignKey(Wears, on_delete=models.CASCADE, null= True)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cart',
        null=True,
        blank=True
    )
    session_key = models.CharField(max_length=40, null=True, blank=True)

    class Meta:
        unique_together = ('user', 'product', 'session_key')

    def __str__(self):
        if self.user:
            return f"{self.user.username} - {self.product.productName} - {self.quantity}"
        else:
            return f"Guest User-{self.session_key} - {self.product.productName} - {self.quantity}"



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



class Shipping(models.Model):
    statusChoices = [
        ('Preparing','Preparing'),
        ('Packaging','Packaging'),
        ('Shipping','Shipping'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='shippings', null=True, blank=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    product = models.ForeignKey('Wears', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    payment_method = models.CharField(max_length=100)
    delivery_time_from = models.DateField(null=True, blank=True) 
    delivery_time_to = models.DateField(null=True, blank=True) 
    customer_name = models.CharField(max_length=100, null=True)
    customer_address = models.CharField(max_length=200, null=True)
    customer_phone = models.CharField(max_length=20, null=True)
    customer_email = models.EmailField(null=True, blank=True)
    shippingStatus = models.CharField(max_length=20, choices=statusChoices, default='Preparing', null=True, blank=True)

    def __str__(self):
        if self.user is None:
            return f"{self.session_key} - {self.product.productName} - {self.quantity} - {self.payment_method}"
        return f"{self.user} - {self.product.productName} - {self.quantity} - {self.payment_method}"
    


class UserReview(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='review', null=True, blank=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    wear = models.ForeignKey('Wears', on_delete=models.CASCADE)
    message = models.TextField(null=True)
    rating = models.IntegerField(null=True)

    def __str__(self):
        return f"Rating: {self.rating} - {self.message[:50]}..."


class ShippedItems(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    product = models.CharField(max_length=100, blank=True)
    quantity = models.IntegerField(null=True)
    customerName = models.CharField(max_length=100, null=True)
    customerPhone = models.CharField(max_length=100, null=True)
    customerEmail = models.EmailField(blank=True, null=True)
    receivedDate = models.DateField(default=timezone.now)


    def __str__(self) -> str:
        return f"{self.product} - {self.receivedDate}" 


class CouponCode(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discountPercent = models.IntegerField(null=True, blank=True, help_text="Enter the percentage amount you are willing to provide")
    discountAmount = models.IntegerField(null=True, blank=True, help_text="Enter the discount amount you are willing to provide")

    def __str__(self):
        return f"Code: {self.code} - Discount Percentage: {self.discountPercent} - Discount Amount: {self.discountAmount}"