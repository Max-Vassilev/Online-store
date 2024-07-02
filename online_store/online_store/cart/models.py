from django.db import models
from online_store.core.models import TechItem

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    tech_item = models.ForeignKey(TechItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
