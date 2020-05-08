from django import forms
from .models import Expense


class ExpenseSearchForm(forms.ModelForm):
    GROUPING = ('date',)
    grouping = forms.ChoiceField(
        choices=[('', '')] + list(zip(GROUPING, GROUPING))
    )

    class Meta:
        model = Expense
        fields = ('name', 'category', 'date',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False
