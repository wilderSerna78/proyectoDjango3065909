from django.contrib import admin
from .models import MechanicalWatch, QuartzWatch, SmartWatch, Customer, Employee, Supplier, Service


# =====================/ Registro de modelos de relojes /===================== #
@admin.register(MechanicalWatch)
class MechanicalWatchAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'type_of_machinery', 'winding_type')
    search_fields = ('brand', 'model', 'type_of_machinery')
    list_filter = ('winding_type',)


@admin.register(QuartzWatch)
class QuartzWatchAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'type_of_machinery', 'battery_life')
    search_fields = ('brand', 'model', 'type_of_machinery')
    list_filter = ('battery_life',)


@admin.register(SmartWatch)
class SmartWatchAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'type_of_machinery', 'os', 'connectivity')
    search_fields = ('brand', 'model', 'os')
    list_filter = ('os', 'connectivity')


# ========================/ Registro de modelos de personas /================= #
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'identification', 'email', 'phone')
    search_fields = ('name', 'identification', 'email')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'identification', 'post', 'salary', 'phone')
    search_fields = ('name', 'identification', 'post')


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'identification', 'company', 'phone')
    search_fields = ('name', 'company')


# =====================/ Registro de modelo Service /========================== #
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_type', 'status', 'customer', 'received_date', 'delivery_date', 'cost')
    search_fields = ('service_type', 'customer__name')
    list_filter = ('status', 'watch_type', 'received_date', 'delivery_date')
