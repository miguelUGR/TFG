# Generated by Django 2.2.6 on 2020-02-11 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desarrollo', '0019_auto_20200210_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='solicitudAstro',
            field=models.BooleanField(default=False, verbose_name='Solicita ser Usuario AstroFisico'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='image',
            field=models.ImageField(default='usuarios/default_image.png', upload_to='usuarios/'),
        ),
    ]
