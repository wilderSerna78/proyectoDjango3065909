# Generated by Django 5.1.7 on 2025-04-02 14:36

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_Name', models.CharField(max_length=100)),
                ('_Identification', models.CharField(max_length=20, unique=True)),
                ('_Phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_Name', models.CharField(max_length=100)),
                ('_Identification', models.CharField(max_length=20, unique=True)),
                ('_Phone', models.CharField(max_length=20)),
                ('post', models.CharField(max_length=50)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MechanicalWatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_Brand', models.CharField(max_length=100)),
                ('_Type_of_machinery', models.CharField(max_length=50)),
                ('_Model', models.CharField(max_length=100)),
                ('winding_type', models.CharField(choices=[('manual', 'Manual'), ('automatic', 'Automático')], default='manual', max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuartzWatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_Brand', models.CharField(max_length=100)),
                ('_Type_of_machinery', models.CharField(max_length=50)),
                ('_Model', models.CharField(max_length=100)),
                ('battery_life', models.IntegerField(default=2)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SmartWatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_Brand', models.CharField(max_length=100)),
                ('_Type_of_machinery', models.CharField(max_length=50)),
                ('_Model', models.CharField(max_length=100)),
                ('os', models.CharField(default='Desconocido', max_length=50)),
                ('connectivity', models.CharField(default='No especificado', max_length=100)),
            ],
            options={
                'verbose_name': 'Reloj Inteligente',
                'verbose_name_plural': 'Relojes Inteligentes',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_Name', models.CharField(max_length=100)),
                ('_Identification', models.CharField(max_length=20, unique=True)),
                ('_Phone', models.CharField(max_length=20)),
                ('company', models.CharField(max_length=100)),
                ('products', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watch_type', models.CharField(choices=[('MechanicalWatch', 'Reloj Mecánico'), ('QuartzWatch', 'Reloj de Cuarzo'), ('SmartWatch', 'Reloj Inteligente')], max_length=20)),
                ('service_type', models.CharField(max_length=100)),
                ('status', models.CharField(default='Pendiente', max_length=50)),
                ('observations', models.TextField(blank=True, null=True)),
                ('parts_used', models.TextField(blank=True, null=True)),
                ('received_date', models.DateField(default=django.utils.timezone.now)),
                ('delivery_date', models.DateField(blank=True, null=True)),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.customer')),
                ('mechanical_watch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='services.mechanicalwatch')),
                ('quartz_watch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='services.quartzwatch')),
                ('smart_watch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='services.smartwatch')),
            ],
        ),
    ]
