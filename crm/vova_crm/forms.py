from django.contrib.admin.widgets import AdminDateWidget
from django import forms
from .models import *


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = [
            'source'
        ]


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'name'
        ]


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = [
            'name'
        ]


class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = [
            'name'
        ]


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'phone_number',
            'email',
            'company',
            'region'
        ]

        widgets = {
            'email': forms.EmailInput
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'date_of_receipt',
            'last_contact_date',
            'source',
            'customer',
            'conversion_goal',
            'status',
            'comment',
            'date_scheduled_call',
            'user',
        ]

        widgets = {
            'last_contact_date': AdminDateWidget(),
            'date_scheduled_call': AdminDateWidget(),
            'date_of_receipt': AdminDateWidget()
        }
