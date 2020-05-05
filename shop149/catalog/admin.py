from django.contrib import admin
from .models import Pharmacy, Pill, Category, FarmGroup


@admin.register(Pharmacy)
class PharmacyAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(FarmGroup)
class FarmGroupAdmin(admin.ModelAdmin):
    pass        


class PillAdmin(admin.ModelAdmin):  
    search_fields = ('title',)
    list_display = ('title', 'batch_number', 'price', 'balance', 'last_update')
    list_filter = ('pharmacy', 'is_active',)   
admin.site.register(Pill, PillAdmin)
