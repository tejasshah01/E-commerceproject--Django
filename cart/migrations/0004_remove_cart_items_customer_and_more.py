# Generated by Django 4.2.5 on 2023-10-05 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_remove_cart_items_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart_items',
            name='Customer',
        ),
        migrations.RemoveField(
            model_name='cart_items',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='cart_items',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='cart_items',
            name='updated_on',
        ),
    ]
