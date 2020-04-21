from django.contrib import admin
from Rental.models import CountryModel,StateModel
# Register your models here.

class ShowCountry(admin.ModelAdmin):
    list_display = ['name','code']
class ShowState(admin.ModelAdmin):
    list_display = ['name','code','country']

admin.site.register(CountryModel,ShowCountry)
admin.site.register(StateModel,ShowState)