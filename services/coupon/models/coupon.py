from django.db import models
class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.code} ({self.discount_rate}%)"