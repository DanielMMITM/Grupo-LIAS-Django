# Generated by Django 4.0.4 on 2022-06-14 02:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('wagtailcore', '0066_collection_management_permissions'),
        ('home', '0067_alter_serviciospage_descripción_1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviciospage',
            name='Descripción_1',
        ),
        migrations.RemoveField(
            model_name='serviciospage',
            name='Descripción_2',
        ),
        migrations.RemoveField(
            model_name='serviciospage',
            name='Texto_1_columna_1',
        ),
        migrations.RemoveField(
            model_name='serviciospage',
            name='Texto_1_columna_2',
        ),
        migrations.RemoveField(
            model_name='serviciospage',
            name='Texto_2_columna_1',
        ),
        migrations.RemoveField(
            model_name='serviciospage',
            name='Texto_2_columna_2',
        ),
        migrations.RemoveField(
            model_name='serviciospage',
            name='Título_columna_1',
        ),
        migrations.RemoveField(
            model_name='serviciospage',
            name='Título_columna_2',
        ),
        migrations.RemoveField(
            model_name='serviciospage',
            name='Título_de_ventana',
        ),
    ]
