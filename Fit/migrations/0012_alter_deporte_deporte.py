# Generated by Django 4.0.6 on 2022-09-11 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fit', '0011_alter_deporte_deporte_metas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deporte',
            name='Deporte',
            field=models.CharField(choices=[('840 ', 'Ciclismo'), ('770 ', 'Natacion'), ('560 ', 'Correr'), ('320', 'Gimnasio'), ('870', 'Crossfit')], max_length=20),
        ),
    ]
