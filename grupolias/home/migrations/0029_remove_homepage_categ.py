# Generated by Django 4.0.4 on 2022-05-23 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_commentspage_commentspagecarouselcomments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='categ',
        ),
    ]