from django.contrib import admin
from .models import MechanicalWatch, QuartzWatch, SmartWatch, Customer, Employee, Supplier, Service


# Register your models here.
admin.site.register(MechanicalWatch)
admin.site.register(QuartzWatch)
admin.site.register(SmartWatch)
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Supplier)
admin.site.register(Service)
