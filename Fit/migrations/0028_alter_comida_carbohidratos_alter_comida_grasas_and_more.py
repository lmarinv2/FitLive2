# Generated by Django 4.0.6 on 2022-11-09 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fit', '0027_remove_comida_azucar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comida',
            name='Carbohidratos',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='comida',
            name='Grasas',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='comida',
            name='Proteina',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='comida',
            name='calorias_Comida',
            field=models.IntegerField(blank=True, max_length=30, null=True),
        ),
    ]