from django.test import TestCase

from ..models import Category, Expense
from .utils import create_test_categories
from ..utils import get_expenses_amount


class ExpensesViewsUtilitiesTestCase(TestCase):
    """Tests for Expenses views utilities"""

    def setUp(self) -> None:
        """Set up for Expenses views utilities tests"""
        create_test_categories()

    def test_get_expenses_amount(self) -> None:
        """
        Test if a get_expenses_amount returns proper amount of expenses
        """
        category = Category.objects.first()
        result = get_expenses_amount(category)
        self.assertEqual(
            result, Expense.objects.filter(category=category).count()
        )
