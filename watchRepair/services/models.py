from django.db import models
from django.utils import timezone


# ========================/ Base models for watches. /========================= #
class Watch(models.Model):
    _Brand = models.CharField(max_length=100)
    _Type_of_machinery = models.CharField(max_length=50)
    _Model = models.CharField(max_length=100)

    class Meta:
        abstract = True  # Modelo abstracto para evitar crear tabla en la BD

    @property
    def brand(self):
        return self._Brand
    
    @property
    def type_of_machinery(self):
        return self._Type_of_machinery
    
    @property
    def model(self):
        return self._Model
    
    
    def general_maintenance(self, extra_info=""):
        return f"Mantenimiento realizado en el reloj {self._Brand} {self._Model} ({self._Type_of_machinery}). {extra_info}"

    def get_information(self):
        return f"{self._Brand} {self._Model} - Tipo: {self._Type_of_machinery}" 

    def __str__(self):
        return self.get_information()


# ===========================/ Clases hijas de Watch /=========================== #
class MechanicalWatch(Watch):
    WINDING_CHOICES = [("manual", "Manual"), ("automatic", "Automático")]
    winding_type = models.CharField(max_length=10, choices=WINDING_CHOICES, default="manual")

    def general_maintenance(self):
        return f"Se ha realizado calibración ({self.winding_type}), limpieza y lubricación en el reloj {self._Brand} {self._Model} ({self._Type_of_machinery})."


class QuartzWatch(Watch):
    battery_life = models.IntegerField(default=2)  # Vida útil de la batería en años.

    def general_maintenance(self):
        return f"Se ha realizado limpieza y cambio de batería en el reloj {self._Brand} {self._Model} ({self._Type_of_machinery})."


class SmartWatch(Watch):
    os = models.CharField(max_length=50, default="Desconocido")  # Sistema operativo
    connectivity = models.CharField(max_length=100, default="No especificado")  # Tipos de conectividad

    def general_maintenance(self):
        return f"Se ha realizado actualización de software y revisión de sensores en el reloj {self._Brand} {self._Model} ({self._Type_of_machinery})."

    class Meta:
        verbose_name = "Reloj Inteligente"
        verbose_name_plural = "Relojes Inteligentes"


# ========================/ Base models for person. /========================= #
class Person(models.Model):
    _Name = models.CharField(max_length=100)
    _Identification = models.CharField(max_length=20, unique=True)
    _Phone = models.CharField(max_length=20)

    class Meta:
        abstract = True

    @property
    def name(self):
        return self._Name

    @property
    def identification(self):
        return self._Identification

    @property
    def phone(self):
        return self._Phone

    def __str__(self):
        return f"{self._Name} - ID: {self._Identification} - Tel: {self._Phone}"


# ===========================/ Clases hijas de Person /=========================== #
class Customer(Person):
    email = models.EmailField(unique=True)


class Employee(Person):
    post = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)


class Supplier(Person):
    company = models.CharField(max_length=100)
    products = models.TextField()


# ========================/ Modelo de Servicios corregido /========================= #
class Service(models.Model):
    WATCH_CHOICES = [
        ("MechanicalWatch", "Reloj Mecánico"),
        ("QuartzWatch", "Reloj de Cuarzo"),
        ("SmartWatch", "Reloj Inteligente"),
    ]
    
    watch_type = models.CharField(max_length=20, choices=WATCH_CHOICES)
    mechanical_watch = models.ForeignKey(MechanicalWatch, on_delete=models.SET_NULL, null=True, blank=True)
    quartz_watch = models.ForeignKey(QuartzWatch, on_delete=models.SET_NULL, null=True, blank=True)
    smart_watch = models.ForeignKey(SmartWatch, on_delete=models.SET_NULL, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default="Pendiente")
    observations = models.TextField(blank=True, null=True)
    parts_used = models.TextField(blank=True, null=True)
    received_date = models.DateField(default=timezone.now)
    delivery_date = models.DateField(blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def complete_service(self):
        self.status = "Terminado"
        self.delivery_date = timezone.localdate()
        self.save()

    def __str__(self):
        return f"Servicio: {self.service_type} - Estado: {self.status} - Cliente: {self.customer._Name}"
