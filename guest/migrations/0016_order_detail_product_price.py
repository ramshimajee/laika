# Generated by Django 5.0.4 on 2024-05-30 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0015_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_detail',
            name='product_price',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]