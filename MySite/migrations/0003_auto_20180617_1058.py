# Generated by Django 2.0b1 on 2018-06-17 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0002_goodsinfo_goods_sales'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GoodsInfo',
            new_name='Goods',
        ),
    ]
