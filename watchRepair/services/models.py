from django.db import models
from datetime import date


# =============================/ Create your models here. /================================== #
class Watch(models.Model):
    brand = models.CharField(max_length=100)
    type_of_machinery = models.CharField(max_length=50)
    model = models.CharField(max_length=100)

    class Meta:
        abstract = True     # Esto convierte a Watch en una clase abstrata para que Watch no se cree como una tabla independiente.

    def __str__(self):
        return f"Marca: {self.brand}, Tipo: {self.type_of_machinery}, Modelo: {self.model}"
    
# Modelos especificos de relojes
class MechanicalWatch(Watch):
    winding_type = models.CharField(max_length=50) # Tipo reloj Manual o Automático.

class QuartzWatch(Watch):
    batery_life = models.IntegerField() # Vida de la bateria duracion en años.

class SmartWatch(Watch):
    os = models.CharField(max_length=50) # Sistema operativo
    connectivity = models.CharField(max_length=100) #Tipos de conectividad


# ===============================/ Modelos base para personas /================================== #
class Person(models.Model):
    name = models.CharField(max_length=100)
    identification = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=20)

    class Meta:
        abstract = True     # Esto convierte a Person en una clase abstrata para que Person no se cree como una tabla independiente.

    def __str__(self):
        return f"Nombre: {self.name}, ID: {self.identification}, Telefono: {self.phone}"
    

# Modelos especificos de personas
class Customer(Person):
    email = models.EmailField(unique=True)

class Employee(Person):
    post = models.CharField(max_length=100) # Cargo
    salary = models.DecimalField(max_digits=10, decimal_places=2)

class Supplier(Person):
    company = models.CharField(max_length=100)
    products = models.TextField() # Lista de productos separados por comas



# ===============================/ Modelo de servicio /================================== #
class Service(models.Model):
    Watch = models.ForeignKey(Watch, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default="Pendiente")
    observations = models.TextField(blank=True, null=True)
    parts_used = models.TextField(blank=True, null=True) #Lista de repuestos usados
    received_date = models.DateField(default=date.today)
    delivery_date = models.DateField(blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def complete_Service(self):
        self.status = "Terminado"
        self.delivery_date = date.today()
        self.save()

    def __str__(self):
        return f"Servicio: {self.service_type} | Cliente: {self.customer.name} | Reloj: {self.Watch.brand} - {self.watch.model} | Estado: {self.status} | Costo: ${self.cost}"
    