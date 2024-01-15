
from django import forms
from products.models import Products, Purchase, Return
from django.core.exceptions import ValidationError


class AddProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('name', 'description','price', 'image', 'quantity')

class ChangeProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('name', 'description','price', 'image', 'quantity')

class BuyProductsForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ('user','product', 'count')


    def clean(self):
        cleaned_data = super().clean()
        count = cleaned_data.get('count')
        product_quantity = self.cleaned_data.get('product').quantity 
        if count > product_quantity:
            raise ValidationError('There are not enough goods right now. Please, choose fewer goods.')
        return cleaned_data

##    def __init__(self, *args, **kwargs):
##        super(BuyProductsForm, self).__init__(*args, **kwargs)
##
##        for field_name, field in self.fields.items():
##           if field_name == 'count' or field_name == 'product':
##               continue  
##            field.widget.attrs['disabled'] = 'disabled'

class ReturnProductsForm(forms.ModelForm):
    class Meta:
        model = Return
        fields = ('purchase',)