from django.contrib import admin

# Register your models here.
from .models import CommercialOffice, MeterReading


class CommercialOfficeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','telephone')


admin.site.register(CommercialOffice, CommercialOfficeAdmin)


class MeterReadingAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'contract_number','commercial_office_id', 'route', 'number', 'reading','reading_date')


admin.site.register(MeterReading, MeterReadingAdmin)

