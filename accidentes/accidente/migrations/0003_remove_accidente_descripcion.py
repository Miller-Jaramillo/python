# Generated by Django 4.1.1 on 2022-11-17 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accidente", "0002_accidente_descripcion"),
    ]

    operations = [
        migrations.RemoveField(model_name="accidente", name="descripcion",),
    ]
