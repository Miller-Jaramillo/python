# Generated by Django 4.1.1 on 2022-10-31 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("personas", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="personas", old_name="TipoVictima", new_name="tipoVictima",
        ),
    ]
