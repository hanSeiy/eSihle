from django import forms
from .models import Invoice


class OnlineOrder(forms.ModelForm):
    name = forms.CharField(max_length=60, widget=forms.TextInput(
        attrs = {
            'placeholder': 'Name',
            'class': 'form-control',
            'name': 'name'
        }
    ))
    surname = forms.CharField(max_length=60, widget=forms.TextInput(
        attrs = {
            'placeholder': 'Surname',
            'class': 'form-control',
            'name': 'surname'
        }
    ))
    address = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs = {
            'placeholder': 'Location/Address',
            'class': 'form-control',
            'name': 'address'
        }
    ))
    contact = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs = {
            'placeholder': 'Contact no.',
            'class': 'form-control',
            'name': 'contact'           
        }
    ))
    quantity = forms.IntegerField(widget=forms.NumberInput(
        attrs = {
            'placeholder': 'Quantity',
            'class': 'form-control',
            'name': 'quantity'
        }
    ))
    class Meta:
        model = Invoice
        fields = '__all__'
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.sub_total = instance.quantity * 75
        if commit:
            instance.save()
        return instance