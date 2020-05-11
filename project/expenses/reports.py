from collections import OrderedDict
from decimal import Decimal
from typing import Dict

from django.db.models import Sum, Value
from django.db.models.functions import TruncMonth
from django.db.models.functions import Coalesce
from django.db.models.query import QuerySet


def summary_per_category(queryset) -> OrderedDict:
    """Summarizes how much money was spend in different categories"""
    return OrderedDict(sorted(
        queryset
        .annotate(category_name=Coalesce('category__name', Value('-')))
        .order_by()
        .values('category_name')
        .annotate(s=Sum('amount'))
        .values_list('category_name', 's')
    ))


def summary_per_year_month(queryset) -> OrderedDict:
    """Summarizes how much money was spent in different months"""
    return OrderedDict(sorted(
        queryset
        .annotate(
            year_month=TruncMonth('date'),
        )
        .order_by()
        .values('year_month')
        .annotate(sum=Sum('amount'))
        .values_list('year_month', 'sum')
    ))


def summary_overall(queryset: QuerySet) -> Dict[str, Decimal]:
    """Summarizes how much money was spent"""
    amount_sum = sum([value[0] for value in queryset.values_list('amount')])

    return {'overall': amount_sum}
