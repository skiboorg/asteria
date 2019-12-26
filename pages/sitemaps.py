from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import *


class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return ['index']

    def location(self, item):
        return reverse(item)


class ServicesSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5
    def items(self):
        return ServiceName.objects.all()
    def lastmod(self, obj):
        return obj.created_at



