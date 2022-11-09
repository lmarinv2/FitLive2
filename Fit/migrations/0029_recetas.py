# Generated by Django 4.0.6 on 2022-11-09 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Fit', '0028_alter_comida_carbohidratos_alter_comida_grasas_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recetas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(choices=[('1', 'Huevos rancheros con pico de gallo'), ('2', 'Ensalada de Pollo'), ('3', 'Pancakes de banano'), ('4', 'Tostada'), ('5', 'Pasta Alfredo'), ('6', 'Papas al Horno'), ('7', 'Smoothie de banano'), ('8', 'Carne y brocoli')], max_length=100)),
                ('Tiempo', models.IntegerField(max_length=100)),
                ('Ingredientes', models.JSONField()),
                ('Preparacion', models.TextField()),
                ('Calorias', models.IntegerField(max_length=1000)),
                ('Fecha', models.DateField(blank=True, null=True)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Fit.registro')),
            ],
        ),
    ]
