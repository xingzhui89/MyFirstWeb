from django.shortcuts import render
from django.http import HttpResponse
from MyFirstWeb import trans
from MySite.models import Goods
from django.db.models import Q

# Create your views here.
# def index(request):
#     return HttpResponse('啊，这是我的第一次！')

def index(request):
    return render(request,'index.html')

def translate(request):
    from_lang=request.GET['from_lang']
    to_lang=request.GET['to_lang']
    text=request.GET['words']
    return HttpResponse(trans.trans(text,from_lang,to_lang))

def translate2(request,words,from_lang,to_lang):
    return HttpResponse(trans.trans(words,from_lang,to_lang))

def news_list(request,news_type):
    news_dict={'economic': '经济', 'sport': '体育'}
    news_titles=[]
    if news_type=='economic':
        news_titles=[
            ('12/5', '作者成为全国首富。'),
            ('12/4', '作者成为全省首富。'),
            ('12/3', '作者成为全市首富。'),
            ('12/2', '作者成为镇里首富。'),
            ('12/1', '作者成为村里首富。')
        ]
    return render(request,'news_list.html',{'news_type': news_dict[news_type],'news_titles':news_titles})

def filter_test(request):
    return render(request,'filter.html',{'letters':'abc','number':1})

def index1(request):
    return render(request,'index_1.html')

def searchAll(request):
    goods_list=Goods.objects.all()
    return render(request,'search_result.html',{'goods_list':goods_list})

def searchname(request):
    goods_name=request.GET['goods_name']
    goods_list=Goods.objects.filter(goods_name=goods_name)
    # goods_list = Goods.objects.get(goods_name=goods_name)# 查询满足条件的一个结果（查询到多个结果时异常）
    # goods_list = Goods.objects.filter(goods_name__contains=goods_name)  # 模糊匹配搜索关键字
    return render(request,'search_result.html',{'goods_list':goods_list})

def searchprice(request):
    min_price=request.GET['min_price']
    max_price=request.GET['max_price']
    goods_list=Goods.objects.filter(goods_price__gt=min_price,goods_price__lt=max_price)
    # goods_list = Goods.objects.filter(Q(goods_price=0.5) | Q(goods_price=2.4)) # 满足任何一个条件
    return render(request,'search_result.html',{'goods_list':goods_list})

def searchsort(request):
    sort = {'all_asc': Goods.objects.order_by('goods_price'),  # 查询全部结果后升序排列
            'all_desc': Goods.objects.order_by('-goods_price'),  # 查询全部结果后降序排列
            'result_asc': Goods.objects.filter(goods_price__lt='5').order_by('goods_price')  # 对某一查询结果排序
            }
    return render(request, 'search_result.html', {'goods_list': sort[request.GET['sort']]})


