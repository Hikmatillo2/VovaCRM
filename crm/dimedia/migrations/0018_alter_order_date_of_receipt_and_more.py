# Generated by Django 4.2.1 on 2023-06-01 12:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dimedia', '0017_alter_customer_email_alter_customer_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_of_receipt',
            field=models.DateField(default=datetime.datetime(2023, 6, 1, 12, 1, 56, 323117), verbose_name='Дата создания обращения'),
        ),
        migrations.AlterField(
            model_name='order',
            name='last_contact_date',
            field=models.DateField(default=datetime.datetime(2023, 6, 1, 12, 1, 56, 323130), verbose_name='Дата последнего контакта с клиентом'),
        ),
    ]
