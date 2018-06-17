import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MyFirstWeb.settings")
django.setup()

from MySite.models import Goods
with open('data','r',encoding='utf-8') as file:
    for line in file:
        lst=line.strip().split(',')
        state=Goods.objects.create(goods_name=lst[0],goods_number=lst[1],goods_price=lst[2])
        print(state)