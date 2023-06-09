# Generated by Django 4.2.1 on 2023-05-16 11:24

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('dimedia', '0002_alter_phonenumber_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonenumber',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=12, region='RU', unique=True, verbose_name='Номер телефона'),
        ),
    ]
