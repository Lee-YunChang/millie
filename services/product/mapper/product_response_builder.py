from decimal import Decimal
from typing import List

from domain.product.dto import ProductDetailDto, ProductDto
from domain.product.entity.entity import Product
from services.category.mapper.category_response_builder import CategoryResponseBuilder


class ProductResponseBuilder:

    @classmethod
    def build_product_response(cls, product: Product) -> dict:
        response = {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': cls.format_decimal(product.price),
            'category': CategoryResponseBuilder.build_category_response(product.category),
            'discount_rate': cls.format_decimal(product.discount_rate),
            'coupon_applicable': product.coupon_applicable,
        }

        return response

    @classmethod
    def build_product_list_response(cls, products: List[ProductDto]) -> List[dict]:
        return [cls.build_product_response(product) for product in products]

    @classmethod
    def build_product_detail_response(cls, productDetailDto: ProductDetailDto) -> dict:
        response = {
            'id': productDetailDto.id,
            'name': productDetailDto.name,
            'description': productDetailDto.description,
            'original_price': productDetailDto.original_price,
            'discounted_price': productDetailDto.discounted_price,
            'final_price': productDetailDto.final_price,
            'category': CategoryResponseBuilder.build_category_response(productDetailDto.category),
            'coupon_applicable': productDetailDto.coupon_applicable,
        }

        if productDetailDto.discount_rate is not None:
            response['discount_rate'] = productDetailDto.discount_rate

        return response

    @staticmethod
    def format_decimal(value: Decimal) -> str:
        return f"{value:,.2f}"
