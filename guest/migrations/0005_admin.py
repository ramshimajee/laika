# Generated by Django 5.0.4 on 2024-05-21 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0004_alter_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('adminid', models.AutoField(primary_key=True, serialize=False)),
                ('adminusername', models.CharField(max_length=100)),
                ('adminpassword', models.CharField(max_length=100)),
            ],
        ),
    ]
