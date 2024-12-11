# services/product/builders/product_response_builder.py

from decimal import Decimal
from typing import Optional
from domain.product.domain.entity import Product
from django.utils import timezone
from django.conf import settings


class ProductResponseBuilder:

    @classmethod
    def build_product_response(cls,
                               product: Product) -> dict:
        response = {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': cls.format_decimal(product.price),
            'category_id': product.category_id,
            'discount_rate': cls.format_decimal(product.discount_rate),
        }

        return response

    @staticmethod
    def format_decimal(value: Decimal) -> str:
        return f"{value:,.2f}"
