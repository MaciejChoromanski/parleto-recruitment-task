from typing import Tuple, Dict

from django.core.handlers.wsgi import WSGIRequest
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.views.generic import DeleteView, DetailView
from django.views.generic.list import ListView

from .forms import ExpenseSearchForm, CategorySearchForm
from .models import Expense, Category
from .reports import (
    summary_per_category,
    summary_per_year_month,
    summary_overall,
)
from .utils import get_expenses_amount


class ExpenseListView(ListView):
    """List view for Expense model"""
    model = Expense
    paginate_by = 5

    def get_context_data(
            self, *, object_list: QuerySet = None, **kwargs
    ) -> Dict:
        """Returns context for the expenses list"""
        queryset = object_list if object_list is not None else self.object_list

        form = ExpenseSearchForm(self.request.GET)
        if form.is_valid():
            name = form.cleaned_data.get('name', '').strip()
            if name:
                queryset = queryset.filter(name__icontains=name)

            categories = form.cleaned_data['categories']
            if categories:
                queryset = queryset.filter(category__in=categories)

            date = form.cleaned_data['date']
            if date:
                queryset = queryset.filter(date=date)

            sort_by = form.cleaned_data['sort_by']
            queryset = self._get_ordered_queryset(queryset, sort_by)

            group_by = form.cleaned_data['group_by']
            queryset = self._get_ordered_queryset(queryset, group_by, '-pk')

            self.paginate_by = form.cleaned_data['items_per_page'] or 5

        return super().get_context_data(
            form=form,
            object_list=queryset,
            total_objects=queryset.count(),
            summary_per_category=summary_per_category(queryset),
            summary_per_year_month=summary_per_year_month(queryset),
            summary_overall=summary_overall(queryset),
            **kwargs
        )

    @staticmethod
    def _get_params(param_str: str) -> Tuple[str, str]:
        """Return params for sorting and grouping operations"""
        if not param_str:
            return '', ''

        sort_params = param_str.split(':')
        if len(sort_params) == 1:
            return '', sort_params[0]

        prefix = '' if sort_params[1].strip() == 'asc' else '-'

        return prefix, sort_params[0]

    def _get_ordered_queryset(
            self, queryset: QuerySet, order_params: str, *ordering: str
    ) -> QuerySet:
        """
        Returns ordered queryset or the same queryset
        if no ordering was requested
        """
        prefix, category = self._get_params(order_params)
        if category == 'category':
            return queryset.order_by(
                f'{prefix}category__name', *ordering
            )
        elif category == 'date':
            return queryset.order_by(
                f'{prefix}date', *ordering
            )
        else:
            return queryset


class CategoryListView(ListView):
    """List view for the Category model"""
    model = Category
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs) -> Dict:
        """Returns context for the categories list"""
        queryset = object_list if object_list is not None else self.object_list

        form = CategorySearchForm(self.request.GET)
        if form.is_valid():
            name = form.cleaned_data.get('name', '').strip()
            if name:
                queryset = queryset.filter(name__icontains=name)

            self.paginate_by = form.cleaned_data['items_per_page'] or 5

        for category in queryset:
            category.expenses = get_expenses_amount(category)

        return super().get_context_data(
            form=form,
            object_list=queryset,
            total_objects=queryset.count(),
            **kwargs
        )


class CategoryDeleteView(DeleteView):
    """Delete view for the Category"""
    model = Category
    template_name = 'expenses/model_delete.html'

    def get_context_data(self, **kwargs) -> Dict:
        """Returns context for the category deletion"""
        return super().get_context_data(
            categories_expenses=get_expenses_amount(self.get_object()),
            **kwargs
        )

    def delete(
            self, request: WSGIRequest, *args, **kwargs
    ) -> HttpResponseRedirect:
        """Deletes all Expenses related to deleted Category"""
        Expense.objects.filter(category=self.get_object()).delete()

        return super().delete(request, *args, **kwargs)


class CategoryDetailView(DetailView):
    """Detail view for the Category"""
    model = Category
    template_name = 'expenses/category_detail.html'

    def get_context_data(self, **kwargs) -> Dict:
        """Returns context for the category deletion"""
        category = self.get_object()
        queryset = Expense.objects.filter(category=category)

        return super().get_context_data(
            category=category,
            categories_expenses=get_expenses_amount(self.get_object()),
            summary_per_year_month=summary_per_year_month(queryset),
            **kwargs
        )
