# Generated by Django 5.0.2 on 2024-02-18 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_alter_car_power_alter_car_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='status',
            field=models.BooleanField(default=True, editable=False, verbose_name='Статус машины'),
        ),
    ]