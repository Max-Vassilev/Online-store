from django.db import models

class TechItem(models.Model):
    CATEGORY_CHOICES = [
        ('tv', 'TV'),
        ('computer', 'Computer'),
        ('laptop', 'Laptop'),
        ('phone', 'Phone'),
        ('tablet', 'Tablet'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    image_url = models.URLField()

    def __str__(self):
        return self.name

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    tech_item = models.ForeignKey(TechItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
