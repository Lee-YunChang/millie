from dataclasses import dataclass, replace
from decimal import Decimal
from typing import Optional
from domain.product.entity.entity import Product
from domain.coupon.entity.entity import Coupon

@dataclass(frozen=True)
class ProductAggregate:
    product: Product
    coupon: Optional[Coupon] = None

    def apply_coupon(self, coupon: Coupon) -> 'ProductAggregate':

        if not self.product.coupon_applicable:
            raise ValueError("This product does not allow coupon application.")
        return replace(self, coupon=coupon)

    def original_price(self) -> Decimal:
        return self.product.price

    def discounted_price(self) -> Decimal:

        if self.product.discount_rate <= Decimal('0.00'):
            return self.product.price

        multiplier = (Decimal('100.00') - self.product.discount_rate) / Decimal('100.00')

        return (self.product.price * multiplier).quantize(Decimal('0.01'))

    def final_price(self) -> Decimal:

        discounted = self.discounted_price()

        if self.coupon is None or self.coupon.discount_rate <= Decimal('0.00'):
            return discounted

        multiplier = (Decimal('100.00') - self.coupon.discount_rate) / Decimal('100.00')

        return (discounted * multiplier).quantize(Decimal('0.01'))