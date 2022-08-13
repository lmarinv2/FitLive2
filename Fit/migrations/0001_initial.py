# Generated by Django 4.0.6 on 2022-08-13 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
                ('fecha_nacimiento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]