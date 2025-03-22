from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone  # Importar timezone de Django

# =============================/ Create your models here. /================================== #
class Watch(models.Model):
    brand = models.CharField(max_length=100)
    type_of_machinery = models.CharField(max_length=50)
    model = models.CharField(max_length=100)

    class Meta:
        abstract = True  # Esto convierte a Watch en una clase abstracta para que no se cree como una tabla independiente.

    def __str__(self):
        return f"Marca: {self.brand}, Tipo: {self.type_of_machinery}, Modelo: {self.model}"

# Modelos específicos de relojes
class MechanicalWatch(Watch):
    winding_type = models.CharField(max_length=50, blank=True, null=True)  # Tipo reloj Manual o Automático.

class QuartzWatch(Watch):
    battery_life = models.IntegerField()  # Vida de la batería en años.

class SmartWatch(Watch):
    os = models.CharField(max_length=50)  # Sistema operativo
    connectivity = models.CharField(max_length=100)  # Tipos de conectividad


# ===============================/ Modelos base para personas /================================== #
class Person(models.Model):
    name = models.CharField(max_length=100)
    identification = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=20)

    class Meta:
        abstract = True  # Esto convierte a Person en una clase abstracta para que no se cree como una tabla independiente.

    def __str__(self):
        return f"Nombre: {self.name}, ID: {self.identification}, Teléfono: {self.phone}"

# Modelos específicos de personas
class Customer(Person):
    email = models.EmailField(unique=True)

class Employee(Person):
    post = models.CharField(max_length=100)  # Cargo
    salary = models.DecimalField(max_digits=10, decimal_places=2)

class Supplier(Person):
    company = models.CharField(max_length=100)
    products = models.TextField()  # Lista de productos separados por comas


# ===============================/ Modelo de servicio /================================== #
class Service(models.Model):
    watch_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    watch_id = models.PositiveIntegerField()  # Mejor usar PositiveIntegerField
    watch = GenericForeignKey('watch_type', 'watch_id')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default="Pendiente")
    observations = models.TextField(blank=True, null=True)
    parts_used = models.TextField(blank=True, null=True)  # Lista de repuestos usados
    received_date = models.DateField(default=timezone.now)  # Usar timezone.now()
    delivery_date = models.DateField(blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def complete_Service(self):
        self.status = "Terminado"
        self.delivery_date = timezone.now().date()  # Manejar zonas horarias correctamente
        self.save()
