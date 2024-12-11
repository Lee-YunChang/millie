import uuid
from typing import Optional

from rest_framework import status
from rest_framework.views import APIView

from domain.product.use_case.product import ProductUseCase
from services.coupon.repo.coupon import CouponRepoImpl
from services.product.mapper.product_response_builder import ProductResponseBuilder
from services.product.repo.product import ProductRepoImpl
from utils.response import APIResponse


class ProductView(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._product_use_case = ProductUseCase(ProductRepoImpl(), CouponRepoImpl())
        self._res_builder = ProductResponseBuilder()

    def get(self, request, category_id: Optional[int] = None):

        products = self._product_use_case.get_products(category_id)
        response = self._res_builder.build_product_list_response(products)

        return APIResponse(
            status.HTTP_200_OK,
            data = response
        )


class ProductDetailView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._product_use_case = ProductUseCase(ProductRepoImpl(), CouponRepoImpl())
        self._res_builder = ProductResponseBuilder()


    def get(self, request, product_id:int, coupon_code:uuid):

        product_detail = self._product_use_case.get_product_detail(product_id, coupon_code)

        return APIResponse(
            status.HTTP_200_OK,
            data=product_detail
        )