# Generated by Django 4.2.1 on 2023-07-13 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0008_contactotrabajo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ArtistaPubli',
            new_name='Categoria',
        ),
        migrations.RenameField(
            model_name='categoria',
            old_name='nombreO',
            new_name='nombreC',
        ),
        migrations.RenameField(
            model_name='obra',
            old_name='artistaPubli',
            new_name='categoria',
        ),
        migrations.AlterField(
            model_name='contactotrabajo',
            name='CV',
            field=models.ImageField(null=True, upload_to='contactotrabajo'),
        ),
        migrations.AlterField(
            model_name='contactotrabajo',
            name='foto',
            field=models.ImageField(null=True, upload_to='contactotrabajo'),
        ),
    ]