# Generated by Django 2.2.2 on 2020-02-02 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='FarmGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Фармгруппа',
                'verbose_name_plural': 'Фармгруппы',
            },
        ),
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
                ('address', models.CharField(max_length=128, verbose_name='Адрес')),
                ('phone_number', models.CharField(max_length=32, verbose_name='Номер телефона')),
                ('pharm_code', models.CharField(max_length=15, null=True, unique=True, verbose_name='Код Аптеки')),
            ],
            options={
                'verbose_name': 'Аптека',
                'verbose_name_plural': 'Аптеки',
            },
        ),
        migrations.CreateModel(
            name='Pill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_code', models.CharField(max_length=50, verbose_name='Код номенклатуры')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('batch_number', models.CharField(max_length=256, verbose_name='Партия')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('balance', models.FloatField(verbose_name='Остаток')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('mnn', models.CharField(max_length=100, verbose_name='МНН')),
                ('is_resept', models.BooleanField(default=False, verbose_name='Признак рецептурного')),
                ('is_life', models.BooleanField(default=False, verbose_name='ЖНВЛС')),
                ('date_valid', models.DateTimeField(verbose_name='Срок годности')),
                ('brand', models.CharField(max_length=200, verbose_name='Бренд')),
                ('price_deli', models.PositiveSmallIntegerField(verbose_name='Цена поставки')),
                ('scancode', models.CharField(max_length=20, verbose_name='Штрихкод')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Category')),
                ('farm_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.FarmGroup')),
                ('pharmacy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Pharmacy', verbose_name='Аптека')),
            ],
            options={
                'verbose_name': 'Препарат',
                'verbose_name_plural': 'Препараты',
            },
        ),
    ]
