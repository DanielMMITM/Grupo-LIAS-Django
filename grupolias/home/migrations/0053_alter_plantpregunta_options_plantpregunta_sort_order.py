# Generated by Django 4.0.4 on 2022-05-29 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0052_alter_plantpregunta_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plantpregunta',
            options={'ordering': ['sort_order']},
        ),
        migrations.AddField(
            model_name='plantpregunta',
            name='sort_order',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
    ]
