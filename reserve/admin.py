from django.contrib import admin
from .models import *

class reserveAdmin(admin.ModelAdmin):

    fieldsets = [
        (u'예약', {'fields':['user',]}),
        (u'호텔', {'fields': ['hotel',]}),
        (u'예약정보', {'fields': ['party','startday','days' ]}),

                 ]

    list_filter = ['hotel__name','startday','date']

    list_display = ['user', 'hotel', 'party','startday','days','date']

    search_fields = ['user__username','hotel__name']




admin.site.register(hotel)
admin.site.register(reservation, reserveAdmin)
