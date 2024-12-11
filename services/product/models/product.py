from django.db import models

from services.category.models import Category

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    discount_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    coupon_applicable = models.BooleanField(default=False)

    class Meta:
        db_table = 'product'
    def __str__(self):
        return self.name
