# Generated by Django 5.1.1 on 2024-10-07 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solpedcaf', '0007_etapa_de_fructificacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='etapa_de_floracion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('tipo', models.CharField(max_length=10)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='modulos')),
            ],
        ),
        migrations.AlterField(
            model_name='etapa_de_crecimiento',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='modulos'),
        ),
        migrations.AlterField(
            model_name='etapa_de_fructificacion',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='modulos'),
        ),
        migrations.AlterField(
            model_name='etapa_de_plantacion',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='modulos'),
        ),
    ]