# Generated by Django 4.0.4 on 2022-05-20 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_rename_separador_de_servicios_homepage_separador_anuncios_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='Logo_barra_de_navegación',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='Navegación_1',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='Navegación_2',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='Navegación_3',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='Navegación_4',
        ),
    ]
