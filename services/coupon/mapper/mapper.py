from domain.coupon.entity.entity import Coupon
from services.coupon.models import Coupon as CouponModel


class CouponMapper:
    @staticmethod
    def to_coupon(coupon: CouponModel) -> Coupon:
        return Coupon(
            code=coupon.code,
            discount_rate=coupon.discount_rate
        )
