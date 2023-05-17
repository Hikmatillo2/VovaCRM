from django.contrib import admin
from import_export.admin import ExportActionMixin
from .forms import *


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


@admin.register(Order)
class OrderAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = [
        'id',
        'customer',
        'conversion_goal_',
        'source',
        'date_of_receipt',
        'last_contact_date',
        'date_scheduled_call',
        'comment_',
        'status',
        'region'
    ]

    def region(self, order: Order):
        return str(order.customer.region.name)

    def comment_(self, order: Order):
        return str(order.comment)[0:65] + '...'

    def conversion_goal_(self, order: Order):
        return str(order.conversion_goal)[0:65] + '...'

    region.short_description = 'Регион'

    form = OrderForm

    search_fields = [
        'id',
        'status__name',
        'source__source',
        'status__name',
        'customer__email',
        'comment',
        'customer__phone_number',
        'customer__email',
        'customer__region__name',
        'customer__company__name',
    ]
