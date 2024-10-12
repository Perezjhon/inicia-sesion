# Generated by Django 5.1.1 on 2024-10-06 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solpedcaf', '0003_plagas_y_enfermedades'),
    ]

    operations = [
        migrations.CreateModel(
            name='etapa_de_crecimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('tipo', models.CharField(max_length=10)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='modulos/plagas_y_enfermedades')),
                ('urlDestino', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]