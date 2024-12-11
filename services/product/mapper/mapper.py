# services/product/mappers/product_mapper.py

from domain.product.domain.entity import Product
from services.product.models import Product as ProductModel

class Mapper:

    @staticmethod
    def to_product(product: ProductModel) -> Product:
        return Product(
            id=product.id,
            name=product.name,
            description=product.description,
            price=product.price,
            category_id=product.category_id,
            discount_rate=product.discount_rate
        )
