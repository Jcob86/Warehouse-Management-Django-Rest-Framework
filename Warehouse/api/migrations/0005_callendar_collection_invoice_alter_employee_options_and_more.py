# Generated by Django 4.1.2 on 2022-10-25 15:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_employee_birth_date_employee_position_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Callendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['last_name']},
        ),
        migrations.AlterField(
            model_name='employee',
            name='working_time',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('inventory', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='api.collection')),
            ],
        ),
        migrations.AddField(
            model_name='collection',
            name='featured_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='api.product'),
        ),
    ]
