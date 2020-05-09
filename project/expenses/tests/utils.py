from ..models import Category


def create_test_categories() -> None:
    """Creates 2 categories, used for testing purposes"""
    categories = [
        Category(name='unnecessary'), Category(name='necessary')
    ]
    Category.objects.bulk_create(categories)


def get_category(name: str) -> Category:
    """Returns a category with a given name"""
    return Category.objects.get(name=name)
