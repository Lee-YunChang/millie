from _decimal import Decimal
from dataclasses import dataclass
from typing import Optional

from domain.category.entity.entity import Category



@dataclass
class ProductDto:
    id: int
    name: str
    description: Optional[str]
    price: Decimal
    category: Category
    coupon_applicable: bool
    discount_rate: Decimal = Decimal('0.00')

@dataclass
class ProductDetailDto:
    id: int
    name: str
    description: Optional[str]
    original_price: str
    discounted_price: str
    final_price: str
    category: Category
    coupon_applicable: bool
    discount_rate: Optional[str] = None