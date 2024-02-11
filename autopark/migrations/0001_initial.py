# Generated by Django 5.0.2 on 2024-02-11 13:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CarBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Бренд')),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренды',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('lastname', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('birthday', models.DateField(verbose_name='Дата рождения')),
                ('age', models.ImageField(upload_to='', verbose_name='Возраст')),
                ('phone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('email', models.CharField(max_length=40, verbose_name='Эл. почта')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=20, verbose_name='Модели')),
                ('color', models.CharField(choices=[('black', 'Черный'), ('white', 'Белый'), ('red', 'красный'), ('green', 'Зеленый'), ('yellow', 'Желтый'), ('blue', 'Синий')], max_length=20, verbose_name='Цвет')),
                ('power', models.ImageField(upload_to='', verbose_name='Мощность')),
                ('year', models.ImageField(upload_to='', verbose_name='Год выпуска')),
                ('image', models.ImageField(blank=True, null=True, upload_to='cars/', verbose_name='Изображение')),
                ('category', models.CharField(choices=[('econom', 'Эконом'), ('comfort', 'Комфорт'), ('comfort+', 'Комфорт+'), ('business', 'Бизнес'), ('luxe', 'Люкс')], max_length=20, verbose_name='Класс')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='autopark.carbrand', verbose_name='Бренд')),
            ],
            options={
                'verbose_name': 'Машина',
                'verbose_name_plural': 'Машины',
            },
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('lastname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('birthday', models.DateField(verbose_name='Дата рождения')),
                ('age', models.ImageField(editable=False, upload_to='', verbose_name='Возраст')),
                ('passport', models.CharField(max_length=11, verbose_name='Паспорт')),
                ('is_available', models.BooleanField(default=True, verbose_name='Доступность')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Водитель',
                'verbose_name_plural': 'Водители',
            },
        ),
    ]
