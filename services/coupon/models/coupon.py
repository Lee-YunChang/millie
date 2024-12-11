import uuid
from django.db import models

class Coupon(models.Model):
    code = models.UUIDField(default=uuid.uuid4, unique=True)
    discount_rate = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'coupon'
    def __str__(self):
        return f"{self.code} ({self.discount_rate}%)"
