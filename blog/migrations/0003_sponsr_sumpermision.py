# Generated by Django 4.2.3 on 2024-06-12 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_ikon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sponsr_rasm', models.ImageField(blank=True, null=True, upload_to='sponsr_rasm/')),
            ],
        ),
        migrations.CreateModel(
            name='Sumpermision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('name', models.CharField(max_length=100)),
                ('narx', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]