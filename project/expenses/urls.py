from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import path, reverse_lazy
from .models import Expense, Category
from .views import ExpenseListView, CategoryListView, CategoryDeleteView

urlpatterns = [
    path('expense/list/',
         ExpenseListView.as_view(),
         name='expense-list'),
    path('expense/create/',
         CreateView.as_view(
             model=Expense,
             fields='__all__',
             template_name='expenses/model_form.html',
             success_url=reverse_lazy('expenses:expense-list')
         ),
         name='expense-create'),
    path('expense/<int:pk>/edit/',
         UpdateView.as_view(
             model=Expense,
             fields='__all__',
             template_name='expenses/model_form.html',
             success_url=reverse_lazy('expenses:expense-list')
         ),
         name='expense-edit'),
    path('expense/<int:pk>/delete/',
         DeleteView.as_view(
             model=Expense,
             template_name='expenses/model_delete.html',
             success_url=reverse_lazy('expenses:expense-list')
         ),
         name='expense-delete'),
    path('category/list/',
         CategoryListView.as_view(),
         name='category-list'),
    path('category/create/',
         CreateView.as_view(
             model=Category,
             fields='__all__',
             template_name='expenses/model_form.html',
             success_url=reverse_lazy('expenses:category-list')
         ),
         name='category-create'),
    path('category/<int:pk>/edit/',
         UpdateView.as_view(
             model=Category,
             fields='__all__',
             template_name='expenses/model_form.html',
             success_url=reverse_lazy('expenses:category-list')
         ),
         name='category-edit'),
    path('category/<int:pk>/delete/',
         CategoryDeleteView.as_view(
            success_url=reverse_lazy('expenses:category-list')
         ),
         name='category-delete')
]
