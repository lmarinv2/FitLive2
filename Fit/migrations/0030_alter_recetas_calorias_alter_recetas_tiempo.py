# Generated by Django 4.0.6 on 2022-11-09 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fit', '0029_recetas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recetas',
            name='Calorias',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='recetas',
            name='Tiempo',
            field=models.IntegerField(),
        ),
    ]