# Generated by Django 5.0.2 on 2024-02-27 18:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0002_alter_driver_age'),
        ('employees', '0004_car_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarDriver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.car')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drivers.driver', verbose_name='Водитель')),
            ],
        ),
    ]