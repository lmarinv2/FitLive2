# Generated by Django 4.0.6 on 2022-11-11 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fit', '0032_alter_comida_carbohidratos_alter_comida_comida_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recetas',
            name='Nombre',
            field=models.CharField(choices=[('Huevos rancheros con pico de gallo', 'Huevos rancheros con pico de gallo'), ('Ensalada de Pollo', 'Ensalada de Pollo'), ('Pancakes de banano', 'Pancakes de banano'), ('Tostada', 'Tostada'), ('Pasta Alfredo', 'Pasta Alfredo'), ('Papas al Horno', 'Papas al Horno'), ('Smoothie de banano', 'Smoothie de banano'), ('Carne y brocoli', 'Carne y brocoli')], max_length=100),
        ),
    ]
