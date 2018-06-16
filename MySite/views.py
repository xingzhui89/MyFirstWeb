from django.shortcuts import render
from django.http import HttpResponse
from MyFirstWeb import trans


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
    return render(request,'news_list.html',{'news_type': news_dict[news_type]})




