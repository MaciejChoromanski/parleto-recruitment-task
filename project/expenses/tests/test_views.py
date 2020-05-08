from datetime import datetime

from django.test import TestCase, Client
from django.urls import reverse

from .utils import create_test_categories, get_category
from ..models import Expense

EXPENSES_LIST = reverse('expenses:expense-list')


class ExpenseListViewTestCase(TestCase):
    """Tests for ExpenseListView"""

    def setUp(self) -> None:
        """Set up for the ExpenseListView tests"""
        create_test_categories()
        expenses = [
            Expense(category=get_category('unnecessary'), name='Hybrid car',
                    amount=1, date=datetime(2020, 5, 4)),
            Expense(category=get_category('necessary'), name='Electric car',
                    amount=1, date=datetime(2020, 5, 8)),
        ]
        Expense.objects.bulk_create(expenses)
        self.client = Client()

    def test_get_context_data_no_date_provided(self) -> None:
        """
        Tests what get_context_data returns when provided with no data
        Expected result: all expenses
        """
        payload = {
            'name': '',
            'date': '',
            'grouping': '',
            'categories': [],
        }
        result = self.client.get(EXPENSES_LIST, payload)
        self.assertEqual(
            len(result.context[-1]['object_list']), 2
        )

    def test_get_context_data_date_provided(self) -> None:
        """
        Tests what get_context_data returns when provided with data
        Expected result: expense with a given data
        """
        payload = {
            'name': '',
            'date': '2020-05-08',
            'grouping': '',
            'categories': [],
        }
        result = self.client.get(EXPENSES_LIST, payload)
        self.assertEqual(
            len(result.context[-1]['object_list']), 1
        )

    def test_get_context_data_multiple_categories_provided(self) -> None:
        """
        Tests what get_context_data returns when provided with <1 categories
        Expected result: all expenses
        """
        payload = {
            'name': '',
            'date': '',
            'grouping': '',
            'categories': [
                get_category('unnecessary').id,
                get_category('necessary').id
            ],
        }
        result = self.client.get(EXPENSES_LIST, payload)
        self.assertEqual(
            len(result.context[-1]['object_list']), 2
        )

    def test_get_context_data_single_category_provided(self) -> None:
        """
        Tests what get_context_data returns when provided with single category
        Expected result: expenses with a given category
        """
        payload = {
            'name': '',
            'date': '',
            'grouping': '',
            'categories': [get_category('necessary').id],
        }
        result = self.client.get(EXPENSES_LIST, payload)
        self.assertEqual(
            len(result.context[-1]['object_list']), 1
        )
