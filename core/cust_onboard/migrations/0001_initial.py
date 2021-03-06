# Generated by Django 3.1.8 on 2022-05-09 04:26

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('cust_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cust_type', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)])),
                ('billing_add', models.CharField(max_length=200)),
                ('shipping_add', models.CharField(max_length=200)),
                ('reference_form', models.CharField(max_length=50)),
                ('gst_no', models.CharField(max_length=15)),
                ('payment_term', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100)])),
                ('delivery_term', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100)])),
                ('comments', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'orders',
            },
        ),
    ]
