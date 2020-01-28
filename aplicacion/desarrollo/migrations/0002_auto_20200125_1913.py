# Generated by Django 2.2.6 on 2020-01-25 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desarrollo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscripciones',
            name='Observaciones_id',
        ),
        migrations.RemoveField(
            model_name='inscripciones',
            name='observatorios_id',
        ),
        migrations.RemoveField(
            model_name='observacion',
            name='observatorios',
        ),
        migrations.AddField(
            model_name='inscripciones',
            name='Observacion',
            field=models.ManyToManyField(to='desarrollo.Observacion'),
        ),
        migrations.AddField(
            model_name='inscripciones',
            name='observatorios',
            field=models.ManyToManyField(to='desarrollo.Observatorio'),
        ),
    ]