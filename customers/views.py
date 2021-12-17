from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import CustomerForm
from .models import Customer


class CustomersListView(ListView):
    model = Customer
    paginate_by = 6
    template_name = 'customers/customers_list.html'

    def get_queryset(self):
        search = self.request.GET.get('search')
        if search:
            object_list = self.model.objects.filter(
                Q(first_name__icontains=search) |
                Q(last_name__icontains=search) |
                Q(area_code__icontains=search) |
                Q(phone_number__icontains=search) |
                Q(email__icontains=search) |
                Q(country__icontains=search) |
                Q(state__icontains=search) |
                Q(city__icontains=search)
            )
        else:
            object_list = self.model.objects.all()
        return object_list


class CustomerCreateView(CreateView):
    template_name = 'customers/customer.html'
    form_class = CustomerForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('customers:customers-list')


class CustomerUpdateView(UpdateView):
    template_name = 'customers/customer.html'
    form_class = CustomerForm

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Customer, id=id)

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('customers:customers-list')


class CustomerDeleteView(DeleteView):
    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Customer, id=id)

    def get_success_url(self):
        return reverse('customers:customers-list')
