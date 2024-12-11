import uuid
from dataclasses import dataclass
from decimal import Decimal

@dataclass(frozen=True)
class Coupon:
    code:uuid
    discount_rate: Decimal