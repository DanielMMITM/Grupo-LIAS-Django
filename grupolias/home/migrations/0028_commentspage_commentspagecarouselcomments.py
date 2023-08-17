# Generated by Django 4.0.4 on 2022-05-23 03:47

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('wagtailimages', '0023_add_choose_permissions'),
        ('home', '0027_homepage_categ'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('Navegación_1', models.TextField(default='')),
                ('Navegación_2', models.TextField(default='')),
                ('Navegación_3', models.TextField(default='')),
                ('Navegación_4', models.TextField(default='')),
                ('Text_EComments', models.TextField(default='')),
                ('Logo_footer', models.TextField(default='')),
                ('Direccion_footer', models.TextField(default='')),
                ('enlacesTitulo', models.TextField(default='')),
                ('Enlace_1', models.TextField(default='')),
                ('Enlace_2', models.TextField(default='')),
                ('Enlace_3', models.TextField(default='')),
                ('tituloContacto', models.TextField(default='')),
                ('Enlace_4', models.TextField(default='')),
                ('Enlace_5', models.TextField(default='')),
                ('Enlace_6', models.TextField(default='')),
                ('Enlace_7', models.TextField(default='')),
                ('tituloRedes', models.TextField(default='')),
                ('Image_EComments', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('Logo_RedSocial1_footer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('Logo_RedSocial2_footer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('Logo_barra_de_navegación', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='CommentsPageCarouselComments',
            fields=[
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Titulo_slideC', models.TextField()),
                ('Texto_slideC', models.TextField()),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='carousel_Comments', to='home.commentspage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]