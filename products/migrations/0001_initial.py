# Generated by Django 4.2.5 on 2023-10-01 06:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category_brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item_name', models.CharField(max_length=100)),
                ('Brand', models.CharField(max_length=100)),
                ('Image', models.ImageField(null=True, upload_to='user_profile')),
                ('Price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('date', models.DateField(default=datetime.date.today)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category_brand')),
            ],
        ),
    ]
