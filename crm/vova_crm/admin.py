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


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = [
        'email'
    ]


@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = [
        'phone_number'
    ]


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
        'phone_numbers',
        'emails',
        'company',
        'region'
    ]

    def emails(self, customer: Customer):
        emails = [email.email for email in customer.email.all()]
        if len(emails) > 1:
            return ', '.join(emails)
        elif len(emails) == 1:
            return emails[0]

    emails.short_description = 'Электронная почта'

    def phone_numbers(self, customer: Customer):
        phone_numbers = [phone_number.email for phone_number in customer.phone_number.all()]
        if len(phone_numbers) > 1:
            return ', '.join(phone_numbers)
        elif len(phone_numbers) == 1:
            return phone_numbers[0]

    emails.short_description = 'Номер телефона'

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
        return mark_safe('<b style="background:{}; border-radius: 4px; display: center">{}</b>'.format(order.status.color, order.status.name))
    status_colored.allow_tags = True
    status_colored.short_description = 'Статус обращения'

    def region(self, order: Order):
        if order.customer.region is not None:
            return str(order.customer.region.name)
        return '-'

    def comment_(self, order: Order):
        if len(order.comment) > 65:
            return str(order.comment.strip())[0:65] + '...'
        return str(order.comment)

    def conversion_goal_(self, order: Order):
        if len(order.conversion_goal) > 65:
            return str(order.conversion_goal.strip())[0:65] + '...'
        return str(order.conversion_goal)
    
    def contacts(self, order: Order):
        phone_numbers = order.customer.phone_number.all()
        emails = order.customer.email.all()

        if len(emails) > 1:
            emails = ', '.join(emails)
        elif len(emails) == 1:
            emails = emails[0]
        else:
            emails = None

        if len(phone_numbers) > 1:
            phone_numbers = ', '.join(phone_numbers)
        elif len(phone_numbers) == 1:
            phone_numbers = phone_numbers[0]
        else:
            phone_numbers = None

        if emails is not None and phone_numbers is not None:
            return f'{emails}\n{phone_numbers}'
        if emails is not None and phone_numbers is None:
            return emails
        if emails is None and phone_numbers is not None:
            return phone_numbers
        return '-'
    
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
