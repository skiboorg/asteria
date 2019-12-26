from django.contrib import admin

from .models import *

class ServiceNameAdmin(admin.ModelAdmin):

    exclude = ['name_slug','name_lower']

    class Meta:
        model = ServiceName
admin.site.register(ServiceName,ServiceNameAdmin)
admin.site.register(SeoTag)
admin.site.register(Master)