from django import forms
from .models import *

class ShopForm(forms.ModelForm):

    class Meta:
        model = Shops
        fields = ('shop_name', 'contact', 'location', 'category', 'contact_person', 'branded', 'email', 'password', 'password2')
