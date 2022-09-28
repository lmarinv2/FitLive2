# Generated by Django 4.0.6 on 2022-09-28 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fit', '0019_comida_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comida',
            name='Nombre',
        ),
        migrations.RemoveField(
            model_name='comida',
            name='dientes',
        ),
        migrations.AddField(
            model_name='comida',
            name='Carbohidratos',
            field=models.CharField(choices=[('100_gramos', 'Porcion'), ('200_gramos', '2_Porciones'), ('300_gramos', '3_porciones'), ('+300_gramos', '+3_porciones')], default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comida',
            name='Comida',
            field=models.CharField(choices=[('Desayuno', 'Desayuno'), ('Almuerzo', 'Almuerzo'), ('Cena', 'Cena'), ('Snacks', 'Snacks')], default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comida',
            name='Proteina',
            field=models.CharField(choices=[('<100_gramos', 'Porcion'), ('<150_gramos', '2_Porcione'), ('<200_gramos', '3_porcione'), ('<250_gramos', '4_porcione'), ('>300_gramos', '5_porcione')], default=1, max_length=100),
            preserve_default=False,
        ),
    ]
