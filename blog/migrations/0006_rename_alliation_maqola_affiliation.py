# Generated by Django 4.2.3 on 2024-06-13 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_firs_name_maqola_first_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maqola',
            old_name='alliation',
            new_name='affiliation',
        ),
    ]
