# Generated by Django 4.2 on 2023-05-05 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudvotaciones', '0002_candidaturas_ciudadanos_votos_delete_framework_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ciudadanos',
            old_name='Edad',
            new_name='edad',
        ),
    ]