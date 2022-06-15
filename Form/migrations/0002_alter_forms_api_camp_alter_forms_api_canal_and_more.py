# Generated by Django 4.0.5 on 2022-06-15 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forms_api',
            name='Camp',
            field=models.CharField(choices=[('', ''), ('ONLINE', 'ONLINE'), ('HARD', 'HARD'), ('SOFT', 'SOFT'), ('TODOS', 'TODOS'), ('ACABADOS', 'ACABADOS')], max_length=10),
        ),
        migrations.AlterField(
            model_name='forms_api',
            name='Canal',
            field=models.CharField(choices=[('', ''), ('EMAIL', 'Email'), ('CELULAR', 'Celular')], max_length=10),
        ),
        migrations.AlterField(
            model_name='forms_api',
            name='Marca',
            field=models.CharField(choices=[('', ''), ('HC', 'Homecenter'), ('CT', 'Constructor')], max_length=10),
        ),
    ]
