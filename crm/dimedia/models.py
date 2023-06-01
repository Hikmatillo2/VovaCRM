from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from colorfield.fields import ColorField


class Email(models.Model):
    email = models.EmailField(
        max_length=128,
        blank=True,
        null=True,
        unique=True,
        verbose_name="Электронная почта"
    )

    def __str__(self):
        return str(self.email)

    class Meta:
        verbose_name = "Электронная почта"
        verbose_name_plural = "Электронные почты"


class PhoneNumber(models.Model):
    phone_number = PhoneNumberField(
        max_length=12,
        unique=True,
        blank=False,
        null=False,
        verbose_name="Номер телефона",
    )

    def __str__(self):
        return str(self.phone_number)

    class Meta:
        verbose_name = "Номер телефона"
        verbose_name_plural = "Номера телефонов"


class Company(models.Model):
    name = models.TextField(
        blank=False,
        null=False,
        unique=True,
        verbose_name="Название компании",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "4. Название компании"
        verbose_name_plural = "4. Названия компаний"


class Status(models.Model):
    name = models.TextField(
        blank=False,
        null=False,
        unique=True,
        verbose_name="Статус обращения"
    )

    color = ColorField(
        blank=False,
        null=False,
        default='#FF0000',
        verbose_name='Цвет статуса'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статус обращения"
        verbose_name_plural = "Статусы обращений"


class Source(models.Model):
    source = models.TextField(
        blank=False,
        null=False,
        unique=True,
        verbose_name="Источник заявки"
    )

    def __str__(self):
        return self.source

    class Meta:
        verbose_name = "Источник заявок"
        verbose_name_plural = "Источники заявок"


class Region(models.Model):
    name = models.TextField(
        blank=False,
        null=False,
        unique=True,
        verbose_name="Регион",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "2. Регион"
        verbose_name_plural = "2. Регионы"


class Customer(models.Model):
    company = models.ForeignKey(
        to=Company,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Компания"
    )

    phone_number = models.ManyToManyField(
        to=PhoneNumber,
        blank=True,
        verbose_name='Номер телефона'
    )

    email = models.ManyToManyField(
        to=Email,
        blank=True,
        verbose_name='Электронная почта'
    )

    region = models.ForeignKey(
        to=Region,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Регион'
    )

    def __str__(self):
        return f"#{self.id} {self.company}"

    class Meta:
        verbose_name = "3. Клиент"
        verbose_name_plural = "3. Клиенты"


class Order(models.Model):
    date_of_receipt = models.DateField(
        blank=False,
        default=datetime.now(),
        null=False,
        verbose_name="Дата создания обращения"
    )

    last_contact_date = models.DateField(
        default=datetime.now(),
        blank=False,
        null=False,
        verbose_name="Дата последнего контакта с клиентом"
    )

    date_scheduled_call = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата запланированного звонка"
    )

    conversion_goal = models.TextField(
        blank=False,
        null=False,
        verbose_name="Цель обращения"
    )

    customer = models.ForeignKey(
        to=Customer,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name="Клиент"
    )

    status = models.ForeignKey(
        to=Status,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name="Статус обращения"
    )

    comment = models.TextField(
        blank=False,
        null=False,
        verbose_name="Комментарий"
    )

    source = models.ForeignKey(
        to=Source,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name="Источник обращения"
    )

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name='Менеджер'
    )

    def __str__(self):
        return f"#{self.id} {self.conversion_goal}"

    class Meta:
        verbose_name = "1. Обращение"
        verbose_name_plural = "1. Обращения"
