from domain.product.entity.entity import Product
from services.category.mapper.mapper import CategoryMapper
from services.product.models import Product as ProductModel

class ProductMapper:

    @staticmethod
    def to_product(product: ProductModel) -> Product:

        category = CategoryMapper.to_category(product.category)

        return Product(
            id=product.id,
            name=product.name,
            description=product.description,
            price=product.price,
            category=category,
            discount_rate=product.discount_rate,
            coupon_applicable=product.coupon_applicable
        )
