# Generated by Django 4.0.6 on 2022-11-11 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fit', '0031_alter_comida_carbohidratos_alter_comida_grasas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comida',
            name='Carbohidratos',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comida',
            name='Comida',
            field=models.CharField(blank=True, choices=[('Desayuno', 'Desayuno'), ('Almuerzo', 'Almuerzo'), ('Cena', 'Cena'), ('Snacks', 'Snacks')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='comida',
            name='Grasas',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comida',
            name='Proteina',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]