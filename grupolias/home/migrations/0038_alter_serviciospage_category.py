# Generated by Django 4.0.4 on 2022-05-24 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_alter_serviciospage_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviciospage',
            name='category',
            field=models.TextField(choices=[('Hogar', 'Hogar'), ('Electricidad', 'Electricidad'), ('Pintura', 'Pintura'), ('Construcción', 'Construccion')], default='Hogar', max_length=12),
        ),
    ]
