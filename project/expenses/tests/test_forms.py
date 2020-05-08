from django.test import TestCase

from .utils import create_test_categories, get_category
from ..forms import ExpenseSearchForm


class ExpenseSearchFormTestCase(TestCase):
    """Tests for ExpenseSearchForm"""

    def setUp(self) -> None:
        """Set up for the ExpenseSearchForm tests"""
        create_test_categories()

    def test_form_validation_valid_date_provided(self) -> None:
        """
        TTests if a form is valid when provided with valid format of date
        """
        data = {
            'name': 'Nintendo DS',
            'date': '2020-05-08',
            'grouping': '',
            'categories': [],
        }
        form = ExpenseSearchForm(data=data)
        self.assertTrue(form.is_valid())

    def test_form_validation_invalid_date_provided(self) -> None:
        """
        Tests if a form is invalid when provided with invalid format of date
        """
        data = {
            'name': 'Colecovision',
            'date': '08-05-2020',
            'grouping': '',
            'categories': [],
        }
        form = ExpenseSearchForm(data=data)
        self.assertFalse(form.is_valid())

    def test_form_validation_multiple_categories_provided(self) -> None:
        """
        Tests if a form is valid when provided with multiple categories
        """
        data = {
            'name': '2001 Okana Gamesphere',
            'date': '',
            'grouping': '',
            'categories': [
                get_category('unnecessary').id,
                get_category('necessary').id
            ],
        }
        form = ExpenseSearchForm(data=data)
        self.assertTrue(form.is_valid())

    def test_form_validation_single_category_provided(self) -> None:
        """
        Tests if a form is valid when provided with a single category
        """
        data = {
            'name': 'PlayStation Portable',
            'date': '',
            'grouping': '',
            'categories': [get_category('necessary').id],
        }
        form = ExpenseSearchForm(data=data)
        self.assertTrue(form.is_valid())
