from typing import List

from domain.product.domain.entity import Product
from domain.product.repositories.product import ProductRepository


class ProductUseCase:

    def __init__(self, repo: ProductRepository):
        self._repo = repo

    def get_products(self, id: int) -> List[Product]:

        product = self._repo.get_products(id)

        return product