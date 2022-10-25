# Generated by Django 4.1.2 on 2022-10-25 13:39

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_employee_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, max_length=31, null=True),
        ),
    ]