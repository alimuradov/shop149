# Generated by Django 2.2.2 on 2020-02-03 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pill',
            name='brand',
            field=models.CharField(max_length=200, null=True, verbose_name='Бренд'),
        ),
        migrations.AlterField(
            model_name='pill',
            name='date_valid',
            field=models.DateTimeField(null=True, verbose_name='Срок годности'),
        ),
        migrations.AlterField(
            model_name='pill',
            name='is_active',
            field=models.BooleanField(default=True, null=True, verbose_name='Активный'),
        ),
        migrations.AlterField(
            model_name='pill',
            name='is_life',
            field=models.BooleanField(default=False, null=True, verbose_name='ЖНВЛС'),
        ),
        migrations.AlterField(
            model_name='pill',
            name='is_resept',
            field=models.BooleanField(default=False, null=True, verbose_name='Признак рецептурного'),
        ),
        migrations.AlterField(
            model_name='pill',
            name='mnn',
            field=models.CharField(max_length=100, null=True, verbose_name='МНН'),
        ),
        migrations.AlterField(
            model_name='pill',
            name='price_deli',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Цена поставки'),
        ),
    ]
