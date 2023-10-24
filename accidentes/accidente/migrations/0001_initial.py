# Generated by Django 4.1.1 on 2022-10-14 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CasoAccidente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100, verbose_name="Nombre")),
                (
                    "descripcion",
                    models.CharField(
                        blank=True,
                        max_length=250,
                        null=True,
                        verbose_name="Descripcion",
                    ),
                ),
                (
                    "create_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Creado"),
                ),
                (
                    "update_at",
                    models.DateTimeField(auto_now=True, verbose_name="Editado"),
                ),
            ],
            options={
                "verbose_name": "Caso accidente",
                "verbose_name_plural": "Casos accidentes",
            },
        ),
        migrations.CreateModel(
            name="TipoAccidente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100, verbose_name="Nombre")),
                (
                    "descripcion",
                    models.CharField(
                        blank=True,
                        max_length=250,
                        null=True,
                        verbose_name="Descripcion",
                    ),
                ),
                (
                    "create_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Creado"),
                ),
                (
                    "update_at",
                    models.DateTimeField(auto_now=True, verbose_name="Editado"),
                ),
            ],
            options={
                "verbose_name": "Tipo accidente",
                "verbose_name_plural": "Tipos accidentes",
            },
        ),
        migrations.CreateModel(
            name="Accidente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("lesion", models.CharField(max_length=100, verbose_name="Lesion")),
                ("fechaHecho", models.DateTimeField(verbose_name="Fecha Hecho")),
                (
                    "create_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Creado"),
                ),
                (
                    "update_at",
                    models.DateTimeField(auto_now=True, verbose_name="Editado"),
                ),
                (
                    "casoAccidente",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accidente.casoaccidente",
                    ),
                ),
                (
                    "tipoAccidente",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accidente.tipoaccidente",
                    ),
                ),
            ],
            options={"verbose_name": "Accidente", "verbose_name_plural": "Accidentes",},
        ),
    ]