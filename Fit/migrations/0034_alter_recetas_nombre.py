# Generated by Django 4.0.6 on 2022-11-14 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fit', '0033_alter_recetas_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recetas',
            name='Nombre',
            field=models.CharField(choices=[('Huevos rancheros con pico de gallo', 'Huevos rancheros con pico de gallo'), ('Ensalada de Pollo', 'Ensalada de Pollo'), ('Pancakes de banano', 'Pancakes de banano'), ('Tostada', 'Tostada'), ('Pasta Alfredo', 'Pasta Alfredo'), ('Papas al Horno', 'Papas al Horno'), ('moothie de banano', 'Smoothie de banano'), ('Carne y brocoli', 'Carne y brocoli')], max_length=100),
        ),
    ]