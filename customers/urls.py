from django.urls import path

from .views import CustomersListView, CustomerCreateView, CustomerUpdateView, CustomerDeleteView

app_name = 'customers'

urlpatterns = [
    path('list/', CustomersListView.as_view(), name='customers-list'),
    path('', CustomerCreateView.as_view(), name='customer-create'),
    path('<int:id>/', CustomerUpdateView.as_view(), name='customer-update'),
    path('<int:id>/delete/', CustomerDeleteView.as_view(), name='customer-delete'),
]
