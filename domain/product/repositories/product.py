from abc import ABC, abstractmethod
from typing import List

from domain.product.domain.entity import Product


class ProductRepository(ABC):

    @abstractmethod
    def get_products(self, id: int) -> List[Product]: pass
