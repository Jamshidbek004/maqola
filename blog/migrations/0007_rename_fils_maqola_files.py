# Generated by Django 4.2.3 on 2024-06-13 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_alliation_maqola_affiliation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maqola',
            old_name='fils',
            new_name='files',
        ),
    ]
