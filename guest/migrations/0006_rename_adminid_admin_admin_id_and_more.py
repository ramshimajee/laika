# Generated by Django 5.0.4 on 2024-05-21 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0005_admin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admin',
            old_name='adminid',
            new_name='admin_id',
        ),
        migrations.RenameField(
            model_name='admin',
            old_name='adminpassword',
            new_name='admin_password',
        ),
        migrations.RenameField(
            model_name='admin',
            old_name='adminusername',
            new_name='admin_username',
        ),
    ]