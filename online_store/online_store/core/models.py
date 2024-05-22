from django.db import models

class TechItem(models.Model):
    CATEGORY_CHOICES = [
        ('TV', 'TV'),
        ('Mobile Phone', 'Mobile Phone'),
        ('PC', 'PC'),
        ('Laptop', 'Laptop'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    image_url = models.URLField(max_length=200, blank=True)  

    def __str__(self):
        return self.name
