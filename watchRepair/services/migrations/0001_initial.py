# Generated by Django 5.1.7 on 2025-03-20 19:30

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('identification', models.CharField(max_length=20, unique=True)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Watch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('type_of_machinery', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='services.person')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
            bases=('services.person',),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='services.person')),
                ('post', models.CharField(max_length=100)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            bases=('services.person',),
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='services.person')),
                ('company', models.CharField(max_length=100)),
                ('products', models.TextField()),
            ],
            bases=('services.person',),
        ),
        migrations.CreateModel(
            name='MechanicalWatch',
            fields=[
                ('watch_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='services.watch')),
                ('winding_type', models.CharField(max_length=50)),
            ],
            bases=('services.watch',),
        ),
        migrations.CreateModel(
            name='QuartzWatch',
            fields=[
                ('watch_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='services.watch')),
                ('batery_life', models.IntegerField()),
            ],
            bases=('services.watch',),
        ),
        migrations.CreateModel(
            name='SmartWatch',
            fields=[
                ('watch_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='services.watch')),
                ('os', models.CharField(max_length=50)),
                ('connectivity', models.CharField(max_length=100)),
            ],
            bases=('services.watch',),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(max_length=100)),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('status', models.CharField(default='Pendiente', max_length=50)),
                ('observations', models.TextField(blank=True, null=True)),
                ('parts_used', models.TextField(blank=True, null=True)),
                ('received_date', models.DateField(default=datetime.date.today)),
                ('delivery_date', models.DateField(blank=True, null=True)),
                ('Watch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.watch')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.customer')),
            ],
        ),
    ]
