from datetime import datetime, date

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
        payload = {'date': ''}
        result = self.client.get(EXPENSES_LIST, payload)
        self.assertEqual(
            len(result.context[-1]['object_list']),
            Expense.objects.all().count()
        )

    def test_get_context_data_date_provided(self) -> None:
        """
        Tests what get_context_data returns when provided with data
        Expected result: expense with a given data
        """
        payload = {'date': '2020-05-08'}
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
            'categories': [
                get_category('unnecessary').id,
                get_category('necessary').id
            ],
        }
        result = self.client.get(EXPENSES_LIST, payload)
        self.assertEqual(
            len(result.context[-1]['object_list']),
            Expense.objects.all().count()
        )

    def test_get_context_data_single_category_provided(self) -> None:
        """
        Tests what get_context_data returns when provided with single category
        Expected result: expenses with a given category
        """
        payload = {
            'categories': [get_category('necessary').id]
        }
        result = self.client.get(EXPENSES_LIST, payload)
        self.assertEqual(
            len(result.context[-1]['object_list']), 1
        )

    def test_get_context_data_sort_by_category_and_ascending(self) -> None:
        """
        Tests what get_context_data returns when sort_by = 'category: asc'
        Expected result: expenses sorted ascending by a category
        """
        payload = {'sort_by': 'category: asc'}
        result = self.client.get(EXPENSES_LIST, payload)
        self.assertEqual(
            result.context[-1]['object_list'][0].category,
            get_category('necessary')
        )

    def test_get_context_data_sort_by_category_and_descending(self) -> None:
        """
        Tests what get_context_data returns when sort_by = 'category: desc'
        Expected result: expenses sorted descending by a category
        """
        payload = {'sort_by': 'category: desc'}
        result = self.client.get(EXPENSES_LIST, payload)
        self.assertEqual(
            result.context[-1]['object_list'][0].category,
            get_category('unnecessary')
        )

    def test_get_context_data_sort_by_date_and_ascending(self) -> None:
        """
        Tests what get_context_data returns when sort_by = 'date: asc'
        Expected result: expenses sorted ascending by a date
        """
        payload = {'sort_by': 'date: asc'}
        result = self.client.get(EXPENSES_LIST, payload)
        self.assertEqual(
            result.context[-1]['object_list'][0].date,
            date(2020, 5, 4)
        )

    def test_get_context_data_sort_by_date_and_descending(self) -> None:
        """
        Tests what get_context_data returns when sort_by = 'date: desc'
        Expected result: expenses sorted descending by a date
        """
        payload = {'sort_by': 'date: desc'}
        result = self.client.get(EXPENSES_LIST, payload)
        self.assertEqual(
            result.context[-1]['object_list'][0].date,
            date(2020, 5, 8)
        )

    def test_get_context_data_group_by_category_ascending(self) -> None:
        """
        Tests what get_context_data returns when group_by = 'category: asc'
        Expected result: expenses grouped ascending by a category
        """
        payload = {'group_by': 'category: asc'}
        result = self.client.get(EXPENSES_LIST, payload)
        self.assertEqual(
            result.context[-1]['object_list'][0].category,
            get_category('necessary')
        )

    def test_get_context_data_group_by_category_descending(self) -> None:
        """
        Tests what get_context_data returns when group_by = 'category: desc'
        Expected result: expenses grouped descending by a category
        """
        payload = {'group_by': 'category: desc'}
        result = self.client.get(EXPENSES_LIST, payload)
        self.assertEqual(
            result.context[-1]['object_list'][0].category,
            get_category('unnecessary')
        )

    def test_get_context_data_group_by_date(self) -> None:
        """
        Tests what get_context_data returns when group_by = 'date'
        Expected result: expenses grouped ascending by a date
        """
        payload = {'group_by': 'date'}
        result = self.client.get(EXPENSES_LIST, payload)
        self.assertEqual(
            result.context[-1]['object_list'][0].date,
            date(2020, 5, 4)
        )
