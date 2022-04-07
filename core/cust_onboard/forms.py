from django import forms
from cust_onboard.models import Order
from django.core.validators import MaxValueValidator


class OrderForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    phone = forms.IntegerField(validators=[MaxValueValidator(9999999999)]) # max cap for phone number length
    billing_add = forms.CharField(max_length=200)
    shipping_add = forms.CharField(max_length=200)
    reference_form = forms.CharField(max_length=50)
    gst_no = forms.CharField(max_length=15) 
    payment_term = forms.IntegerField(validators=[MaxValueValidator(100)])
    delivery_term = forms.IntegerField(validators=[MaxValueValidator(100)])
    comments = forms.CharField(max_length=500)
    
    class Meta:
        model = Order
        fields = "__all__"