# Generated by Django 2.2.6 on 2020-06-26 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('desarrollo', '0002_auto_20200626_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='observatorio',
            name='opcionInscripcion',
        ),
    ]
