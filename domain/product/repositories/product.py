from abc import ABC, abstractmethod
from typing import List, Optional

from domain.product.entity.entity import Product


class ProductRepository(ABC):

    @abstractmethod
    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        pass

    @abstractmethod
    def get_products(self, category_id: Optional[int] = None) -> List[Product]: pass
