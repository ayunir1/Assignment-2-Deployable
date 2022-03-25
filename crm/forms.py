from django import forms
from .models import *


# imported all models


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = (
            'cust_name', 'organization', 'role', 'bldgroom', 'address',
            'city', 'state', 'zipcode', 'email', 'phone'
        )


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = (
            'cust_name', 'service_category', 'description', 'location', 'setup_time',
            'cleanup_time', 'service_charge'
        )


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'cust_name', 'product', 'quantity', 'description', 'charge', 'pickup_time'
        )
