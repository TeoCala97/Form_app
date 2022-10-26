# Generated by Django 4.0.5 on 2022-10-21 20:21

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Form', '0006_remove_forms_api_id_forms_api_ciclo_vida_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forms_api',
            name='Segmento_necesidad',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('', ''), ('CONSTRUCTOR DE JARDINES', 'CONSTRUCTOR DE JARDINES'), ('TBD', 'TBD'), ('VENTA EMPRESA', 'VENTA EMPRESA'), ('TODERO', 'TODERO'), ('PINTOR', 'PINTOR'), ('ELECTRICISTA', 'ELECTRICISTA'), ('ORNAMENTADOR', 'ORNAMENTADOR'), ('MULTIESPECIALIDAD CONTRATISTA', 'MULTIESPECIALIDAD CONTRATISTA'), ('HOGAR', 'HOGAR'), ('MAESTRO', 'MAESTRO'), ('ESPECIALISTA ACABADOS', 'ESPECIALISTA ACABADOS'), ('CARPINTERO', 'CARPINTERO'), ('PLOMERO', 'PLOMERO'), ('NO CONTRUCTOR', 'NO CONTRUCTOR'), ('DECORADOR', 'DECORADOR'), ('ESPECIALISTA DRYWALL', 'ESPECIALISTA DRYWALL')], max_length=212, verbose_name='Segmento Necesidad'),
        ),
        migrations.AlterField(
            model_name='forms_api',
            name='Tienda_frecuente',
            field=models.CharField(choices=[('', ''), ('Dorado', 'DORADO'), ('Avda. 68 Sur Bogota', 'AVDA. 68 SUR BOGOTA'), ('Medellin San Juan', 'MEDELLIN SAN JUAN'), ('Envigado', 'ENVIGADO'), ('Medellin Molinos', 'MEDELLIN MOLINOS'), ('Cali Norte', 'CALI NORTE'), ('AVDA. 68 SUR BOGOTA', 'AVDA. 68 SUR BOGOTA'), ('RIONEGRO', 'RIONEGRO'), ('SUBA', 'SUBA'), ('NORTE BOGOTA', 'NORTE BOGOTA'), ('CALI NORTE', 'CALI NORTE'), ('CARTAGENA LA POPA', 'CARTAGENA LA POPA'), ('Cali Sur', 'CALI SUR'), ('Bello', 'BELLO'), ('Palmira Unicentro', 'PALMIRA UNICENTRO'), ('Yopal', 'YOPAL'), ('Dorado Bogota', 'DORADO BOGOTA'), ('MOSQUERA', 'MOSQUERA'), ('CALIMA BOGOTA', 'CALIMA BOGOTA'), ('CUCUTA', 'CUCUTA'), ('ARMENIA', 'ARMENIA'), ('Cajica', 'CAJICA'), ('TULUA EL RETIRO', 'TULUA EL RETIRO'), ('Ibague', 'IBAGUE'), ('Girardot', 'GIRARDOT'), ('Bucaramanga La Rosita', 'BUCARAMANGA LA ROSITA'), ('TINTAL', 'TINTAL'), ('CALI SUR', 'CALI SUR'), ('CARTAGENA SAN FERNANDO', 'CARTAGENA SAN FERNANDO'), ('Mzls San Rafael', 'MANIZALES SAN RAFAEL'), ('Neiva San Pedro', 'NEIVA SAN PEDRO'), ('Valledupar Guatapuri', 'VALLEDUPAR GUATAPURI'), ('SOACHA', 'SOACHA'), ('BARRANQUILLA CENTRO', 'BARRANQUILLA CENTRO'), ('Cedritos Bogota', 'CEDRITOS BOGOTA'), ('Calima Bogota', 'CALIMA BOGOTA'), ('OAT', 'OAT'), ('VCIO FUNDADORES', 'VILLAVICENCIO FUNDADORES'), ('VENTA DISTANCIA BOGOTA', 'VENTA DISTANCIA BOGOTA'), ('Calle 80 Bogota', 'CALLE 80 BOGOTA'), ('Pereira', 'PEREIRA'), ('HOMECENTER MALLPLAZA NQS', 'HOMCENTER MALLPLAZA NQS'), ('MONTERIA EL RECREO', 'MONTERIA EL RECREO'), ('BARRANQUILLA NORTE', 'BARRANQUILLA NORTE'), ('Medellin Insdustriales', 'MEDELLIN INDUSTRIALES'), ('Centro de Distribucion (900)', 'CENTRO DE DISTRIBUCION (900)'), ('Barranquilla Calle 30', 'BARRANQUILLA CALLE 3O'), ('TUNJA', 'TUNJA'), ('SANTA MARTA BUENAVISTA', 'SANTA MARTA BUENAVISTA')], max_length=30, verbose_name='Tienda Frecuente'),
        ),
    ]
