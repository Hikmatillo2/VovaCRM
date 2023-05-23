from django.contrib import admin
from import_export.admin import ExportActionMixin
from .forms import *
from django.utils.safestring import mark_safe


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
        'name',
        'color',
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
        'user',
        'contacts',
        'conversion_goal_',
        'source',
        'date_of_receipt',
        'last_contact_date',
        'comment_',
        'status_colored',
        'region',
    ]

    def status_colored(self, order: Order):
        return mark_safe('<b style="background:{};">{}</b>'.format(order.status.color, order.status.name))
    status_colored.allow_tags = True
    status_colored.short_description = 'Статус обращения'

    def region(self, order: Order):
        return str(order.customer.region.name)

    def comment_(self, order: Order):
        if len(order.comment) > 65:
            return str(order.comment.strip())[0:65] + '...'
        return str(order.comment)

    def conversion_goal_(self, order: Order):
        if len(order.conversion_goal) > 65:
            return str(order.conversion_goal.strip())[0:65] + '...'
        return str(order.conversion_goal)
    
    def contacts(self, order: Order):
        return f'{str(order.customer.phone_number)}\n{order.customer.email}'
    
    conversion_goal_.short_description = 'Цель обращения'
    contacts.short_description = 'Контакты клиента'
    region.short_description = 'Регион'
    comment_.short_description = 'Комментарий'
    form = OrderForm

    search_fields = [
        'id',
        'status__name',
        'source__source',
        'status__name',
        'customer__email',
        'comment',
        'user__first_name',
        'user__last_name',
        'customer__phone_number',
        'customer__email',
        'customer__region__name',
        'customer__company__name',
    ]
