from django import forms
from .models import Subscription

class SubscriptionForm(forms.Form):
    name = forms.CharField(max_length=60, required=True, label='ชื่อ-นามสกุล')
    email = forms.EmailField(max_length=60, required=True, label='อีเมล')
    accepted = forms.BooleanField(required=True, label='กรุณากดยอมรับ')

class SubscriptionModelForm(forms.ModelForm):
    accepted = forms.BooleanField(required=True, label='กรุณากดยอมรับ')
    class Meta:
        model = Subscription
        fields = ['name', 'email', 'accepted']
        labels = {
            'name': 'ชื่อ-นามสกุล',
            'email': 'อีเมล'
        }