from django.contrib import admin
from import_export.admin import ExportActionMixin
from .forms import *


@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = [
        'phone_number'
    ]

    form = PhoneNumberForm


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = [
        'source'
    ]

    form = SourceForm


@admin.register(Company)
class CompanyAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = [
        'name'
    ]

    form = CompanyForm


@admin.register(Status)
class StatusForm(admin.ModelAdmin):
    list_display = [
        'name'
    ]

    form = StatusForm


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]

    form = RegionForm


@admin.register(Customer)
class CustomerAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = [
        'phone_number',
        'email',
        'company',
        'region'
    ]

    # def phone_number(self, customer: Customer):
    #     return customer.phone_number.phone_number.name
    form = CustomerForm


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'text',
        'date',
    )

    form = CommentForm


@admin.register(Order)
class OrderAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = [
        'id',
        'customer',
        'conversion_goal',
        'source',
        'date_of_receipt',
        'last_contact_date',
        'date_scheduled_call',
        'comments',
        'status',
    ]

    def comments(self, order: Order):
        comments = [program.text for program in order.comment.all()]
        if len(comments) > 1:
            return ', '.join(comments)
        elif len(comments) == 1:
            return comments[0]

    form = OrderForm

    search_fields = [
        'id',
        'status__name',
        'source__source',
        'status__name',
        'customer__email',
        'customer__phone_number',
        'customer__company__name'
        'customer__region__name',
    ]
