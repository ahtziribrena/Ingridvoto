# Generated by Django 4.2 on 2023-05-15 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudvotaciones', '0005_rename_patidoseleccionado_votos_votacion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='votos',
            old_name='votacion',
            new_name='voto',
        ),
    ]
