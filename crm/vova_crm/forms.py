import phonenumber_field.formfields
from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from .models import *
from .widgets import DatePickerInput, TimePickerInput


class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = PhoneNumber
        fields = [
            'phone_number'
        ]

        # widgets = {
        #     'phone_number': PhoneNumberPrefixWidget(),
        # }


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


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'text',
            'date',

        )

        widgets = {
            'date': DatePickerInput(),
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'date_of_receipt',
            'last_contact_date',
            'date_scheduled_call',
            'conversion_goal',
            'customer',
            'status',
            'comment',
            'source'
        ]

        widgets = {
            'last_contact_date': DatePickerInput(),
            'date_scheduled_call': DatePickerInput(),
            'date_of_receipt': DatePickerInput()
        }
