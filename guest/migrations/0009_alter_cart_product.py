# Generated by Django 5.0.4 on 2024-05-22 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0008_rename_product_id_cart_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='product',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
