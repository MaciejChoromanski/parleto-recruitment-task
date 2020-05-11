from .models import Category, Expense


def get_expenses_amount(category: Category) -> int:
    """Returns number of Expenses of a given Category"""
    return Expense.objects.filter(category=category).count()
