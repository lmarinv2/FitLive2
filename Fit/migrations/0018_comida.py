# Generated by Django 4.0.6 on 2022-09-25 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fit', '0017_alter_metas_eleccion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=200)),
                ('Ingredientes', models.TextField()),
                ('Hora', models.DateTimeField()),
            ],
        ),
    ]
