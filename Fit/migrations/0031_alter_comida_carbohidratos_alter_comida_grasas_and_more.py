# Generated by Django 4.0.6 on 2022-11-09 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fit', '0030_alter_recetas_calorias_alter_recetas_tiempo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comida',
            name='Carbohidratos',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='comida',
            name='Grasas',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='comida',
            name='Proteina',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='comida',
            name='calorias_Comida',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
