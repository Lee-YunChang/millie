from rest_framework import status
from rest_framework.views import APIView

from domain.product.use_case.product import ProductUseCase
from services.product.mapper.product_response_builder import ProductResponseBuilder
from services.product.repo.product import ProductRepoImpl
from utils.response import APIResponse


class ProductView(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._product_use_case = ProductUseCase(ProductRepoImpl())
        self._res_builder = ProductResponseBuilder()

    def get(self, request, product_id:int):

        id = product_id

        products = self._product_use_case.get_products(id)

        response = self._res_builder.build_product_response(products)

        return APIResponse(
            status.HTTP_200_OK,
            data = response
        )