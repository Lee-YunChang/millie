
from domain.category.entity.entity import Category

class CategoryResponseBuilder:

    @staticmethod
    def build_category_response(category: Category) -> dict:
        return {
            'id': category.id,
            'name': category.name,
            'description': category.description
        }
