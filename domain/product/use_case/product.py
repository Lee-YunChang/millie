import uuid
from _decimal import Decimal
from typing import List, Optional

from domain.coupon.repositories.coupon import CouponRepository
from domain.product.aggregate.aggregate import ProductAggregate
from domain.product.dto import ProductDetailDTO
from domain.product.entity.entity import Product
from domain.product.repositories.product import ProductRepository


class ProductUseCase:

    def __init__(self, product_repo: ProductRepository, coupon_repo: CouponRepository):
        self._product_repo = product_repo
        self._coupon_repo = coupon_repo

    def get_products(self, category_id: Optional[int] = None) -> List[Product]:
        product = self._product_repo.get_products(category_id)

        return product

    def get_product_detail(self, product_id:int, coupon_code:uuid):

        product = self._product_repo.get_product_by_id(product_id)

        aggregate = ProductAggregate(product=product)

        coupon = self._coupon_repo.get_coupon_by_code(coupon_code)
        if coupon:
            aggregate = aggregate.apply_coupon(coupon)

        original_price = aggregate.original_price()
        discounted_price = aggregate.discounted_price()
        final_price = aggregate.final_price()

        return ProductDetailDTO(
            id=product.id,
            name=product.name,
            description=product.description,
            original_price=str(original_price),
            discounted_price=str(discounted_price),
            final_price=str(final_price),
            category_id=product.category_id,
            coupon_applicable=product.coupon_applicable,
            discount_rate=str(product.discount_rate) if product.discount_rate > Decimal('0.00') else None,
        )

