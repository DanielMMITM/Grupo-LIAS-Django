# Generated by Django 4.0.4 on 2022-05-30 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0056_prueba'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PreguntasCategory',
        ),
        migrations.RemoveField(
            model_name='plantpregunta',
            name='categoría',
        ),
        migrations.AlterField(
            model_name='formfield',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='header',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='Prueba',
        ),
    ]
