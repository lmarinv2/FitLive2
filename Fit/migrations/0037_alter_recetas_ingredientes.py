# Generated by Django 4.0.6 on 2022-11-14 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fit', '0036_alter_recetas_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recetas',
            name='Ingredientes',
            field=models.TextField(),
        ),
    ]