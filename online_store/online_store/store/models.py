from django.db import models

class TechItem(models.Model):
    CATEGORY_CHOICES = [
        ('tv', 'TV'),
        ('pc', 'PC'),
        ('laptop', 'Laptop'),
        ('phone', 'Phone'),
        ('tablet', 'Tablet'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    image_url = models.URLField()

    def __str__(self):
        return self.name

