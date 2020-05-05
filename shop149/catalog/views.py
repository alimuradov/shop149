import json

import re

from datetime import timedelta
from functools import reduce

from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse
from django.db import transaction
from django.db.models import Q
from django.utils import timezone
from django.http import JsonResponse

from bulk_update.helper import bulk_update

from .models import Pharmacy, Pill
from .serializers import PharmacySerializer, PillSerializer


class PharmacyViewSet(viewsets.ModelViewSet):
    queryset = Pharmacy.objects.all().order_by('name')
    serializer_class = PharmacySerializer


class PillList(generics.ListAPIView):
    serializer_class = PillSerializer
    model = serializer_class.Meta.model
    queryset = Pill.objects.all()
    filter_backends = (SearchFilter, )
    search_fields = ('^title',)


    @classmethod
    def get_extra_actions(cls):
        return []


@csrf_exempt
def data_fill(request):
    try:
        jsonBody = request.read()
        data = json.loads(jsonBody.decode("utf-8-sig"))  # Загрузка JSON
    except ValueError:
        return HttpResponse("invalid json")

    pharmacy_code = data.get("pharmacyCode")  # ID аптеки
    pills = data.get("pills")  # Массив номенклатуры
    pills_new = []  # Номенклатура, которой еще нет в бд
    pills_updated = []  # Номенклатура, у которой изменился остаток или цена
    pills_not_changed = []  # Номенклатура без изменений
    pills_db = Pill.objects.filter(pharmacy__pharm_code=pharmacy_code)  # Вся номеклатура бд по ID аптеки
    time_now = timezone.now()  # datetime.now()  # Текущее время
    pills_obj = {}
    for pill in pills_db:  # Словарь вида {Код номенклатуры: [Наименование, цена, остаток], ...}
        batch_tuple = (pill.item_code, pill.batch_number)
        pills_obj[batch_tuple] = pill  # Пример {1:["Нурофен", 15.7, 150], 2:["Но-шпа", 15, 300], ... }
    with transaction.atomic():
        for item in pills:
            batch_tuple = (item['Код'], item['Характеристика'])
            if batch_tuple in pills_obj:  # Ишим код в бд
                pill = pills_obj[batch_tuple]
                if pill.title != item['Номенклатура'].upper() or pill.price != item['Цена'] or pill.balance != item['Остаток'] or pill.batch_number != item['Характеристика']:
                    pill.title = item['Номенклатура'].upper()  # Если изменилось Наименование или цена или остаток, обновляем в БД
                    pill.price = item['Цена']
                    pill.balance = item['Остаток']
                    pill.batch_number = item['Характеристика']
                    pill.last_update = time_now
                    pills_updated.append(pill)
                else:
                    pill.last_update = time_now  # Просто обновляем last_update
                    pills_not_changed.append(pill)
            else:
                pharmacy_my = Pharmacy.objects.get(pharm_code = pharmacy_code)  
                pills_new.append(Pill(pharmacy = pharmacy_my, item_code=item['Код'], title=item['Номенклатура'].upper(), price=item['Цена'],
                                      balance=item['Остаток'], last_update=time_now, is_active=True, batch_number=item['Характеристика']))
                # Код не нашли, добавляем новую строку
    # Применить измения
    Pill.objects.bulk_create(pills_new)
    bulk_update(pills_updated)
    bulk_update(pills_not_changed, update_fields=["last_update"])
    # Ответ для 1с
    return HttpResponse("ok")   


@csrf_exempt
def search(request):
    # http://julienphalip.com/post/2825034077/adding-search-to-a-django-site-in-a-snap
    query = request.GET['q']
    query = re.sub("[^a-zA-Zа-яА-Я0-9-.]", " ", query, re.U).split()  # Разделяем запрос на массив слов

    result = []
    search_time = timezone.now() - timedelta(hours=24)  # datetime.now() - timedelta(hours=3)  # Текущее время - 3 часа
    if query:
        result = Pill.objects. \
                    filter(reduce(lambda x, y: x & y, [Q(title__icontains=word) for word in query]), is_active=True, last_update__gte=search_time). \
                    values('title', 'pharmacy__title', 'pharmacy__phone_number', 'balance', 'price'). \
                    order_by("pharmacy__title")[:300]

    if result:
        return JsonResponse(list(result), safe=False)
    else:
        return JsonResponse(list(), safe=False)

        

