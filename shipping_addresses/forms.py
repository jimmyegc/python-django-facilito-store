
from django.forms import ModelForm
from django import forms

from shipping_addresses.models import ShippingAddress

class ShippingAddressForm(ModelForm):
    class Meta: 
        model = ShippingAddress 
        fields = [
            'line1',
            'line2',
            'city',
            'state',
            'country',
            'postal_code',
            'reference'
        ]
      
        labels = {
            'line1': 'Calle 1',
            'line2': 'Calle 2',
            'city': 'Ciudad',
            'state': 'Estado',
            'country': 'País',
            'postal_code': 'Código postal',
            'reference': 'Referencias'
        }
      
        widgets = {
            'line1': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'placeholder': 'Calle y número',
            }),
            'line2': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'placeholder': 'Calle y número',
            }),
            'city': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'placeholder': 'Ciudad',
            }),
            'state': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'placeholder': 'Estado',
            }),
            'country': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'placeholder': 'Estado',
            }),            
            'postal_code': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'placeholder': 'Código postal',
            }),
            'reference': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'placeholder': 'Estado',
            }),
            
        }