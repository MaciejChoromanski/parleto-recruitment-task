from django.test import TestCase

from .utils import create_test_categories, get_category
from ..forms import ExpenseSearchForm, CategorySearchForm


class ExpenseSearchFormTestCase(TestCase):
    """Tests for ExpenseSearchForm"""

    def setUp(self) -> None:
        """Set up for the ExpenseSearchForm tests"""
        create_test_categories()

    def test_form_validation_valid_date_provided(self) -> None:
        """
        TTests if a form is valid when provided with valid format of date
        """
        data = {'date': '2020-05-08'}
        form = ExpenseSearchForm(data=data)
        self.assertTrue(form.is_valid())

    def test_form_validation_invalid_date_provided(self) -> None:
        """
        Tests if a form is invalid when provided with invalid format of date
        """
        data = {'date': '08-05-2020'}
        form = ExpenseSearchForm(data=data)
        self.assertFalse(form.is_valid())

    def test_form_validation_multiple_categories_provided(self) -> None:
        """
        Tests if a form is valid when provided with multiple categories
        """
        data = {
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
            'categories': [get_category('necessary').id],
        }
        form = ExpenseSearchForm(data=data)
        self.assertTrue(form.is_valid())

    def test_form_validation_valid_sort_by_provided(self) -> None:
        """
        Tests if a form is valid when provided with a valid sort_by
        """
        data = {'sort_by': 'category: asc'}
        form = ExpenseSearchForm(data=data)
        self.assertTrue(form.is_valid())

    def test_form_validation_invalid_sort_by_provided(self) -> None:
        """
        Tests if a form is invalid when provided with a invalid sort_by
        """
        data = {'sort_by': 'not supported: also'}
        form = ExpenseSearchForm(data=data)
        self.assertFalse(form.is_valid())

    def test_form_validation_items_per_page_provided(self) -> None:
        """
        Tests if a form is valid when provided with a items_per_page
        """
        data = {'items_per_page': 3}
        form = ExpenseSearchForm(data=data)
        self.assertTrue(form.is_valid())


class CategorySearchFormTestCase(TestCase):
    """Tests for CategorySearchForm"""

    def test_form_validation_name_provided(self) -> None:
        """
        Tests if a form is valid when provided with a name
        """
        data = {'name': 'category'}
        form = CategorySearchForm(data=data)
        self.assertTrue(form.is_valid())

    def test_form_validation_items_per_page_provided(self) -> None:
        """
        Tests if a form is valid when provided with a items_per_page
        """
        data = {'items_per_page': 3}
        form = CategorySearchForm(data=data)
        self.assertTrue(form.is_valid())
