import uuid
from abc import ABC, abstractmethod
from typing import Optional

from domain.coupon.entity.entity import Coupon


class CouponRepository(ABC):

    @abstractmethod
    def get_coupon_by_code(self, coupon_code: uuid) -> Optional[Coupon]:
        pass
