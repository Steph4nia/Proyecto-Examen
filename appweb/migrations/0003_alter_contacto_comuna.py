# Generated by Django 4.2.1 on 2023-06-26 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0002_obra_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='comuna',
            field=models.IntegerField(),
        ),
    ]
