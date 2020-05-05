from django.db import models

class Pharmacy(models.Model):
    title = models.CharField('Название', max_length=128)
    address = models.CharField('Адрес', max_length=128)
    phone_number = models.CharField('Номер телефона', max_length=32)
    pharm_code = models.CharField('Код Аптеки', max_length=15, unique=True, blank=False, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Аптека'
        verbose_name_plural = 'Аптеки'


class Category(models.Model):
    title = models.CharField('Название', max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Factory(models.Model):
    title = models.CharField('Производитель', max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'        


class FarmGroup(models.Model):
    title = models.CharField('Название', max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фармгруппа'
        verbose_name_plural = 'Фармгруппы'         


class Pill(models.Model):
    pharmacy = models.ForeignKey(Pharmacy, verbose_name='Аптека', on_delete=models.CASCADE)
    item_code = models.CharField('Код номенклатуры', max_length=50)
    title = models.CharField('Название', max_length=256)
    batch_number = models.CharField('Партия', null=True, max_length=256)
    price = models.FloatField('Цена')
    balance = models.FloatField('Остаток')
    last_update = models.DateTimeField('Обновлено', auto_now=True)
    is_active = models.BooleanField('Активный', null=True, default=True)
    mnn = models.CharField('МНН', null=True, max_length=100)
    is_resept = models.BooleanField('Признак рецептурного', null=True, default=False)
    is_life = models.BooleanField('ЖНВЛС', null=True, default=False)
    farm_group = models.ForeignKey(FarmGroup, null=True, on_delete=models.CASCADE)
    date_valid = models.DateTimeField('Срок годности', null=True, auto_now=False)
    brand = models.CharField('Бренд', null=True, max_length=200)
    price_deli = models.PositiveSmallIntegerField('Цена поставки', null=True)
    scancode = models.CharField('Штрихкод', max_length=20, null=True)
    category = models.ForeignKey(Category, null=True, on_delete = models.CASCADE)
    factory = models.ForeignKey(Factory, null=True, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Препарат'
        verbose_name_plural = 'Препараты'
