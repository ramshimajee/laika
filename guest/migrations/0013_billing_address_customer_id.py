# Generated by Django 5.0.4 on 2024-05-27 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0012_rename_city_billing_address_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='billing_address',
            name='customer_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
