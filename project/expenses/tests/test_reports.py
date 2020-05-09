from decimal import Decimal, ROUND_HALF_UP

from django.test import TestCase

from .utils import create_test_expenses
from ..models import Expense
from ..reports import summary_overall


class ReportsTestCase(TestCase):
    """Test reports utilities for the expenses"""

    def setUp(self) -> None:
        """Set up for the reports utilities tests"""
        create_test_expenses()

    def test_summary_overall(self) -> None:
        """Test if summary_overall properly sums amount of expenses"""
        queryset = Expense.objects.all()
        result = summary_overall(queryset)
        self.assertEqual(
            result['overall'],
            Decimal(150.55).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        )
