from django.db import models
from django.conf import settings



class  Category(models.Model):
    CATEGORY_CHOICES = [
        ('SummerWear', 'Summerwear'),
        ('WinterWear', 'Winterwear'),
        ('Western', 'Western'),
        ('Cotton', 'Cotton')
    ]
    categoryName = models.CharField(max_length=100, choices=CATEGORY_CHOICES, unique=True)

    def __str__(self):
        return self.categoryName

class Wears(models.Model):
    summerOrWinterChoices  = [
        ('SummerWear', 'Summerwear'),
        ('WinterWear', 'Winterwear')
    ]
    productId = models.AutoField(primary_key=True)
    summerOrWinter  = models.CharField(max_length=20, choices=summerOrWinterChoices )
    categories = models.ManyToManyField(Category)
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
        return f"{self.productName} - {self.summerOrWinter}"



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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='shippings', null=True, blank=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    product = models.ForeignKey('Wears', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    payment_method = models.CharField(max_length=100)

    customer_name = models.CharField(max_length=100, null=True)
    customer_address = models.CharField(max_length=200, null=True)
    customer_phone = models.CharField(max_length=20, null=True)
    customer_email = models.EmailField(null=True, blank=True)
    def __str__(self):
        return f"{self.user.username} - {self.product.productName} - {self.quantity} - {self.payment_method}"
    


class UserReview(models.Model):
    ratingChoices =  [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='review')
    wear = models.ForeignKey('Wears', on_delete=models.CASCADE)
    message = models.TextField()
    rating = models.IntegerField(choices=ratingChoices)

    def __str__(self):
        return f"Rating: {self.get_rating_display()} - {self.message[:50]}..."

