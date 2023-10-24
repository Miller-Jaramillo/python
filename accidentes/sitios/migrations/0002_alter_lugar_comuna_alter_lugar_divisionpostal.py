# Generated by Django 4.1.1 on 2022-10-31 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sitios", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lugar",
            name="comuna",
            field=models.CharField(
                blank=True, max_length=15, null=True, verbose_name="Comuna"
            ),
        ),
        migrations.AlterField(
            model_name="lugar",
            name="divisionPostal",
            field=models.CharField(max_length=100, verbose_name="Codigo postal"),
        ),
    ]
