from django.views.generic.list import ListView

from .forms import ExpenseSearchForm
from .models import Expense
from .reports import summary_per_category, summary_per_year_month


class ExpenseListView(ListView):
    model = Expense
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
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
            if sort_by:
                sort_params = sort_by.split(':')
                prefix = '' if sort_params[1].strip() == 'asc' else '-'
                if sort_params[0] == 'category':
                    queryset = queryset.order_by(f'{prefix}category__name')
                else:
                    queryset = queryset.order_by(f'{prefix}date')

            group_by = form.cleaned_data['group_by']
            if group_by:
                queryset = queryset.order_by(group_by, '-pk')

        return super().get_context_data(
            form=form,
            object_list=queryset,
            summary_per_category=summary_per_category(queryset),
            summary_per_year_month=summary_per_year_month(queryset),
            **kwargs
        )
