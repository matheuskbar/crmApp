from django import forms

from .models import Customer


class CustomerForm(forms.ModelForm):
    first_name = forms.CharField(label='Primeiro Nome', max_length=30, widget=forms.TextInput(attrs={'class': 'w3-input w3-border w3-section'}))
    last_name = forms.CharField(label='Sobrenome', max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'w3-input w3-border w3-section'}))
    email = forms.EmailField(label='E-mail', max_length=50, widget=forms.TextInput(attrs={'class': 'w3-input w3-border w3-section'}))
    birth_date = forms.DateField(label='Data de Nascimento', widget=forms.DateInput(attrs={'class': 'w3-input w3-border w3-section', 'type': 'date'}))
    area_code = forms.RegexField(
        label='DDD',
        regex=r'^\+?1?[0-9]{2,3}$',
        error_messages={'invalid': 'Número de DDD inválido'},
        max_length=4,
        widget=forms.TextInput(attrs={'class': 'w3-input w3-border w3-section'})
    )
    phone_number = forms.RegexField(
        label='Telefone',
        regex=r'^\+?1?[0-9]{8,10}$',
        error_messages={'invalid': 'Número de telefone inválido'},
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'w3-input w3-border w3-section'})
    )
    country = forms.CharField(label='País', max_length=30, widget=forms.TextInput(attrs={'class': 'w3-input w3-border w3-section'}))
    state = forms.CharField(label='Estado', max_length=30, widget=forms.TextInput(attrs={'class': 'w3-input w3-border w3-section'}))
    city = forms.CharField(label='Cidade', max_length=30, widget=forms.TextInput(attrs={'class': 'w3-input w3-border w3-section'}))

    class Meta:
        model = Customer
        fields = [
            'first_name',
            'last_name',
            'email',
            'birth_date',
            'area_code',
            'phone_number',
            'country',
            'state',
            'city'
        ]
