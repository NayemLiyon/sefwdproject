from django.contrib import admin

from .models import Caruosel
# Register your models here.

class CaruselAdmin(admin.ModelAdmin):
    list_display = ['title','image']
    search_fields = ['title']

admin.site.register(Caruosel, CaruselAdmin)
