# Generated by Django 4.0.4 on 2022-06-14 02:46

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('wagtailimages', '0023_add_choose_permissions'),
        ('home', '0065_rename_thank_you_text_commentpage_texto_de_agradecimiento_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviciospage',
            name='Descripción_1',
            field=wagtail.core.fields.RichTextField(default=''),
        ),
        migrations.AddField(
            model_name='serviciospage',
            name='Descripción_2',
            field=wagtail.core.fields.RichTextField(default=''),
        ),
        migrations.AddField(
            model_name='serviciospage',
            name='Texto_1_columna_1',
            field=models.CharField(default='Visita', max_length=35),
        ),
        migrations.AddField(
            model_name='serviciospage',
            name='Texto_1_columna_2',
            field=models.CharField(default='$200', max_length=35),
        ),
        migrations.AddField(
            model_name='serviciospage',
            name='Texto_2_columna_1',
            field=models.CharField(default='Servicios de mano de obra', max_length=35),
        ),
        migrations.AddField(
            model_name='serviciospage',
            name='Texto_2_columna_2',
            field=models.CharField(default='$400', max_length=12),
        ),
        migrations.AddField(
            model_name='serviciospage',
            name='Título_columna_1',
            field=models.CharField(default='Actividad', max_length=15),
        ),
        migrations.AddField(
            model_name='serviciospage',
            name='Título_columna_2',
            field=models.CharField(default='Precio', max_length=15),
        ),
        migrations.AddField(
            model_name='serviciospage',
            name='Título_de_ventana',
            field=models.CharField(default='COTIZACIONES', max_length=25),
        ),
    ]
