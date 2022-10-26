# Generated by Django 4.0.5 on 2022-10-21 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Form', '0010_remove_forms_api_ciclo_vida_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forms_api',
            name='Segmento_necesidad',
        ),
        migrations.AddField(
            model_name='forms_api',
            name='Segmento_valor',
            field=models.CharField(choices=[('', ''), ('S', 'S'), ('REGULAR', 'REGULAR'), ('VENTA EMPRESA', 'VENTA EMPRESA')], default=None, max_length=20, verbose_name='Segmento Valor'),
            preserve_default=False,
        ),
    ]
