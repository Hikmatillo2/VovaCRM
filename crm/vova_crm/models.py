from datetime import datetime

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

'''
Телефон:
  номер_телефона: строка # unique

Заказчик:
  телефон: Телефон # необязательные поля
  почта: строка # необязательные поля unique
  компания: строка # необязательные поля



Комментарий:
  текст: строка
  дата: дата

Статус:
  статус: строка

Обращение:
  дата_получения_заявки: дата
  дата_последнего_контакта: дата
  дата_запланированного_звонка: дата
  цель_обращения: строка
  заказчик: Заказчик
  статус: Статус
  комментарий: Комментарий
'''


class PhoneNumber(models.Model):
    phone_number = PhoneNumberField(
        max_length=12,
        region='RU',
        unique=True,
        blank=False,
        null=False,
        verbose_name="Номер телефона",
    )

    def __str__(self):
        return str(self.phone_number)

    class Meta:
        verbose_name = "Номер телефоны"
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
        verbose_name = "Название компании"
        verbose_name_plural = "Названия компаний"


class Status(models.Model):
    name = models.TextField(
        blank=False,
        null=False,
        unique=True,
        verbose_name="Статус обращения"
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
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"


class Customer(models.Model):
    phone_number = models.ForeignKey(
        to=PhoneNumber,
        on_delete=models.CASCADE,
        verbose_name="Номер телефона",
    )

    email = models.EmailField(
        max_length=128,
        blank=False,
        null=False,
        unique=True,
        verbose_name="Электронная почта"
    )

    company = models.ForeignKey(
        to=Company,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name="Компания"
    )

    region = models.ForeignKey(
        to=Region,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"#{self.id} {self.company}"

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Comment(models.Model):
    text = models.TextField(
        blank=False,
        null=False,
        verbose_name="Комментарий"
    )

    date = models.DateField(
        blank=False,
        null=False,
        verbose_name="Дата создания комментария"
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Комментарий к обращению"
        verbose_name_plural = "Комментарии к обращениям"


class Order(models.Model):
    date_of_receipt = models.DateField(
        blank=False,
        null=False,
        verbose_name="Дата создания обращения"
    )

    last_contact_date = models.DateField(
        blank=False,
        null=False,
        verbose_name="Дата последнего контакта с клиентом"
    )

    date_scheduled_call = models.DateField(
        blank=False,
        null=False,
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

    comment = models.ManyToManyField(
        to=Comment,
        blank=False,
        null=False,
        verbose_name="Комментарии"
    )

    source = models.ForeignKey(
        to=Source,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name="Источник обращения"
    )

    def __str__(self):
        return f"#{self.id} {self.conversion_goal}"

    class Meta:
        verbose_name = "Обращение"
        verbose_name_plural = "Обращения"
