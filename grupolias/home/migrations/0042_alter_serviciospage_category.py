# Generated by Django 4.0.4 on 2022-05-25 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0041_alter_serviciospage_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviciospage',
            name='category',
            field=models.TextField(choices=[('HOGAR', 'HOGAR'), ('ELECTRICIDAD', 'ELECTRICIDAD'), ('PINTURA', 'PINTURA'), ('CONSTRUCCIÓN', 'CONSTRUCCIÓN')], default='HOGAR', max_length=12),
        ),
    ]
