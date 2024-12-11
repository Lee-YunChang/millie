import uuid
from typing import Optional

from django.core.exceptions import ObjectDoesNotExist

from domain.coupon.entity.entity import Coupon
from domain.coupon.repositories.coupon import CouponRepository
from services.coupon.mapper.mapper import CouponMapper
from services.coupon.models.coupon import Coupon as CouponModel


class CouponRepoImpl(CouponRepository):

    def __init__(self):
        self._mapper = CouponMapper()

    def get_coupon_by_code(self, coupon_code: uuid) -> Optional[Coupon]:

        try:
            coupon_model = CouponModel.objects.get(code=coupon_code)

            coupon = self._mapper.to_coupon(coupon_model)

        except ObjectDoesNotExist:
            return None

        return coupon