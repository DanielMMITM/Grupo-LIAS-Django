# Generated by Django 4.0.4 on 2022-05-20 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_serviciospage_logo_barra_de_navegación_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviciospage',
            name='Titulo_trabajos_hechos',
            field=models.TextField(default=''),
        ),
    ]