from typing import Union, List, Tuple

from django import forms
from .models import Expense, Category


def _get_choices(choices: Union[str, list]) -> List[Tuple[str, str]]:
    """Returns list of choices, used for the ChoiceFields"""
    result = [('', '')]
    if isinstance(choices, str):
        result.append((choices, choices))
    else:
        for choice in choices:
            result.append((choice, choice))

    return result


class ExpenseSearchForm(forms.ModelForm):
    """Form for searching for Expenses"""
    CATEGORIES = ['category: asc', 'category: desc']
    categories = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, queryset=Category.objects.all()
    )
    sort_by = forms.ChoiceField(
        choices=_get_choices(CATEGORIES + ['date: asc', 'date: desc'])
    )
    group_by = forms.ChoiceField(
        choices=_get_choices(CATEGORIES + ['date'])
    )

    class Meta:
        model = Expense
        fields = ('name', 'date',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False
