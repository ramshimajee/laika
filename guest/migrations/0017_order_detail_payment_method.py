# Generated by Django 5.0.4 on 2024-06-06 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0016_order_detail_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_detail',
            name='payment_method',
            field=models.CharField(default=0, max_length=50, verbose_name=''),
            preserve_default=False,
        ),
    ]
