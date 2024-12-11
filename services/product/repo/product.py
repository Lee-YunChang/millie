from typing import List

from domain.product.domain.entity import Product
from domain.product.repositories.product import ProductRepository
from services.product.mapper.mapper import Mapper
from services.product.models import Product as ProductModel
from utils.exceptions import ObjectNotFoundError


class ProductRepoImpl(ProductRepository):

    def __init__(self):
        self._mapper = Mapper()

    def get_products(self, id:int) -> List[Product]:

        try:
            product_model = ProductModel.objects.get(
                id=id
            )
        except ProductModel.DoesNotExist:
            raise ObjectNotFoundError(
                ProductModel,
                message="Dividend does not exists.",
            )
        return self._mapper.to_product(product_model)