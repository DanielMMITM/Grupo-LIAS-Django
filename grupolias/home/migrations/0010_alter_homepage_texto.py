# Generated by Django 4.0.4 on 2022-05-19 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_homepage_texto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='Texto',
            field=models.TextField(default=''),
        ),
    ]
