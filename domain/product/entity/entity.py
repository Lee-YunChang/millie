from dataclasses import dataclass
from decimal import Decimal
from typing import Optional

from domain.category.entity.entity import Category


@dataclass(frozen=True)
class Product:
    id: int
    name: str
    description: Optional[str]
    price: Decimal
    category: Category
    coupon_applicable: bool
    discount_rate: Decimal = Decimal('0.00')

