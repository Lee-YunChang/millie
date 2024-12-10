from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    discount_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)  # 예: 20.00 = 20% 할인
    def __str__(self):
        return self.name

    @property
    def discounted_price(self):
        # 상품 자체의 할인율 적용된 가격 반환
        if self.discount_rate > 0:
            return self.price * (1 - (self.discount_rate / 100))
        return self.price

    def apply_coupon(self, coupon: Coupon):
        # 쿠폰 적용된 최종 가격 계산 로직
        discounted = self.discounted_price
        # 쿠폰 할인도 % 단위
        return discounted * (1 - (coupon.discount_rate / 100))
