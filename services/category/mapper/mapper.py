from domain.category.entity.entity import Category
from services.category.models import Category as CategoryModel


class CategoryMapper:
    def to_category(category_model: CategoryModel) -> Category:
        return Category(
            id=category_model.id,
            name=category_model.name,
            description=category_model.description
        )