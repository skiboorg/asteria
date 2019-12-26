from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *

def index(request):
    try:
        seotag = SeoTag.objects.first()
        pageTitle = seotag.indexTitle
        allServices = ServiceName.objects.all()
        pageDescription = seotag.indexDescription
        pageKeywords = seotag.indexKeywords
    except:
        pageTitle = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
        pageDescription = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
        pageKeywords = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
    return render(request, 'pages/index.html', locals())








def service(request,slug):
    currentService = get_object_or_404(ServiceName, name_slug=slug)
    allServices = ServiceName.objects.all()[:3]
    pageDescription = currentService.page_description
    pageKeywords = currentService.page_keywords
    return render(request, 'pages/service.html', locals())


def robots(request):
    robotsTxt = f"User-agent: *\nDisallow: /admin/\nHost: https://www.buhkosmos174.ru/\nSitemap: https://www.buhkosmos174.ru/sitemap.xml"
    return HttpResponse(robotsTxt, content_type="text/plain")