from typing import List, Optional

from django.core.exceptions import ObjectDoesNotExist

from domain.product.entity.entity import Product
from domain.product.repositories.product import ProductRepository
from services.product.mapper.mapper import Mapper
from services.product.models import Product as ProductModel
from utils.exceptions import ObjectNotFoundError


class ProductRepoImpl(ProductRepository):

    def __init__(self):
        self._mapper = Mapper()

    def get_product_by_id(self, product_id: int) -> Optional[Product]:

        try:
            product_model = ProductModel.objects.get(id=product_id)

            product = self._mapper.to_product(product_model)

        except ObjectDoesNotExist:
            return None

        return product

    def get_products(self, category_id: Optional[int] = None) -> List[Product]:

        try:
            queryset = ProductModel.objects.select_related('category').all()

            if category_id is not None:
                queryset = queryset.filter(category_id=category_id)

            products = [self._mapper.to_product(pm) for pm in queryset]

        except ProductModel.DoesNotExist:
            raise ObjectNotFoundError(
                ProductModel,
                message="Product does not exists.",
            )
        return products
