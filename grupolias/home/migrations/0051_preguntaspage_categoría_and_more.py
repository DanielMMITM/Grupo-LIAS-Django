# Generated by Django 4.0.4 on 2022-05-29 21:31

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0050_remove_preguntascategory_identificador_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='preguntaspage',
            name='categoría',
            field=modelcluster.fields.ParentalManyToManyField(to='home.preguntascategory'),
        ),
        migrations.AlterField(
            model_name='plantpregunta',
            name='categoría',
            field=modelcluster.fields.ParentalManyToManyField(to='home.preguntascategory'),
        ),
    ]
