# Generated by Django 2.1.7 on 2019-06-14 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_system', '0002_auto_20190614_2003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productorder',
            name='paidable_amount',
        ),
    ]
