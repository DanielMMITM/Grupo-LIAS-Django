# Generated by Django 4.0.4 on 2022-05-20 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_homepagecarouselimages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='Separador_de_anuncios',
        ),
    ]
