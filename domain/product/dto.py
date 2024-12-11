from dataclasses import dataclass
from typing import Optional

@dataclass
class ProductDetailDTO:
    id: int
    name: str
    description: Optional[str]
    original_price: str
    discounted_price: str
    final_price: str
    category_id: int
    coupon_applicable: bool
    discount_rate: Optional[str] = None