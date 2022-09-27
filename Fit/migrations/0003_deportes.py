# Generated by Django 4.0.6 on 2022-09-05 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Fit', '0002_remove_registro_nombre_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deportes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Deporte', models.CharField(choices=[('ci', 'Ciclismo'), ('na', 'Natacion'), ('co', 'Correr'), ('gi', 'Gimnasio'), ('cr', 'Crossfit')], max_length=20)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Fit.registro')),
            ],
        ),
    ]