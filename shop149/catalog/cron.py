import time
import pytz
from dbfread import DBF

from django_bulk_update.helper import bulk_update
from django.utils.timezone import now, pytz
from django.db import transaction

from .models import Pill, Pharmacy, Category, Factory, FarmGroup

def import_dbf_job():
    user_timezone = pytz.timezone("Europe/Moscow")
    time_now = now()  # datetime.now()  # Текущее время
    print("начало импорта " + now().astimezone(user_timezone).strftime("%H.%M.%S"))
    pills = DBF('/home/nariman/ost.dbf', encoding='cp866')
    
    pills_new = []  # Номенклатура, которой еще нет в бд
    pills_updated = []  # Номенклатура, у которой изменился остаток или цена
    pills_not_changed = []  # Номенклатура без изменений
    pills_db = Pill.objects.all()  # Вся номеклатура бд по ID аптеки
    
    pills_obj = {}
    for pill in pills_db:  # Словарь вида {Код номенклатуры: [Наименование, цена, остаток], ...}
        batch_tuple = (pill.item_code,  pill.pharmacy)
        pills_obj[batch_tuple] = pill  # Пример {1:["Нурофен", 15.7, 150], 2:["Но-шпа", 15, 300], ... }

    for item in pills:
        
        # try:
        #     valid_date = datetime.datetime.strptime(item['DATEVALID'], '%d.%m.%Y')
        # except ValueError:
        #     valid_date = None


        try:
            pharmacy_my = Pharmacy.objects.get(title=item['NAMEPODR'])
        except Pharmacy.DoesNotExist:
            pharmacy_my = None

        # pharmacy_my = Pharmacy.objects.get(title=item['NAMEPODR'])    
        factory_my, created = Factory.objects.get_or_create(title=item['FACTORY'])

        batch_tuple = (str(item['CODTMC']), pharmacy_my)
        if batch_tuple in pills_obj:  # Ишим код в бд
            pill = pills_obj[batch_tuple]
            if pill.title != item['NAMETMC'].upper() or pill.price != item['PRICE'] or pill.balance != item['OST'] \
                    or pill.factory != item['FACTORY']:
                pill.title = item['NAMETMC'].upper()  # Если изменилось Наименование или цена или остаток, обновляем в БД
                pill.price = item['PRICE']
                pill.balance = item['OST']
                # pill.date_valid = valid_date
                pill.last_update = time_now
                pills_updated.append(pill)
            else:
                pill.last_update = time_now  # Просто обновляем last_update
                pills_not_changed.append(pill)
        else:
            category_my, created = Category.objects.get_or_create(title=item['CATEGORY']) 
            farmgroup_my, created = FarmGroup.objects.get_or_create(title=item['FARMGROUP'])

            
            pills_new.append(Pill(
                pharmacy = pharmacy_my, 
                item_code=item['CODTMC'], 
                title=item['NAMETMC'].upper(), 
                price=item['PRICE'],
                balance=item['OST'], 
                last_update=time_now, 
                is_active=True, 
                mnn = item['MNN'],
                is_resept = item['ISRECEPT'],
                is_life = item['ISLIFE'],
                farm_group = farmgroup_my,
                #date_valid = valid_date,
                brand = item['BRAND'],
                price_deli = item['PRICE'],
                scancode = item['SCANCOD'],
                category = category_my,
                factory = factory_my
                )) 
            # Код не нашли, добавляем новую строку
    # Применить измения
    Pill.objects.bulk_create(pills_new)
    bulk_update(pills_updated)
    bulk_update(pills_not_changed, update_fields=["last_update"])
    # Ответ для 1с
    print("конец импорта " +  time_now.strftime("%H.%M.%S"))
  
#import_dbf_job() 