from django.contrib import admin
from .models import *


class CountryAdmin(admin.ModelAdmin):
    list_display = ('title', 'info', 'banner')


class CountryReceiptAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'country', 'author', 'time_creation')


class CountryCommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'receipt', 'time_creation', 'time_change')


admin.site.register(Country, CountryAdmin)
admin.site.register(CountryReceipt, CountryReceiptAdmin)
admin.site.register(CountryComment, CountryCommentAdmin)
