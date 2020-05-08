from ..models import Category


def create_test_categories():
    categories = [
        Category(name='unnecessary'), Category(name='necessary')
    ]
    Category.objects.bulk_create(categories)


def get_category(name: str):
    return Category.objects.get(name=name)
