from dataclasses import dataclass
from decimal import Decimal
from typing import Optional

@dataclass(frozen=True)
class Product:
    id: int
    name: str
    description: Optional[str]
    price: Decimal
    category_id: int
    coupon_applicable: bool
    discount_rate: Decimal = Decimal('0.00')

