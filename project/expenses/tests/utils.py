from datetime import datetime

from ..models import Category, Expense


def create_test_categories() -> None:
    """Creates 2 categories, used for testing purposes"""
    categories = [
        Category(name='unnecessary'), Category(name='necessary')
    ]
    Category.objects.bulk_create(categories)


def get_category(name: str) -> Category:
    """Returns a category with a given name"""
    return Category.objects.get(name=name)


def create_test_expenses() -> None:
    """Creates 2 expenses, used for testing purposes"""
    create_test_categories()
    expenses = [
        Expense(category=get_category('unnecessary'), name='shirt',
                amount=50.40, date=datetime(2020, 5, 4)),
        Expense(category=get_category('necessary'), name='jeans',
                amount=100.15, date=datetime(2020, 5, 8)),
    ]
    Expense.objects.bulk_create(expenses)
