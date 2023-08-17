# Generated by Django 4.0.4 on 2022-06-14 02:51

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('wagtailimages', '0023_add_choose_permissions'),
        ('home', '0066_serviciospage_descripción_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviciospage',
            name='Descripción_1',
            field=wagtail.core.fields.RichTextField(default='Es posible que el precio cambie dependiendo del tipo de trabajo que se requiera, estos son solo precios de referencia'),
        ),
        migrations.AlterField(
            model_name='serviciospage',
            name='Descripción_2',
            field=wagtail.core.fields.RichTextField(default='*Si aceptan la cotización/el servicio, se descuenta el precio de visita'),
        ),
    ]
