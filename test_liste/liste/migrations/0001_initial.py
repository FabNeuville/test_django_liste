# Generated by Django 5.0.2 on 2024-02-29 11:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prestation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artiste', models.CharField(max_length=50)),
                ('titre_spectacle', models.CharField(max_length=50)),
                ('nb_artiste', models.IntegerField(blank=True, null=True)),
                ('nb_technicien', models.IntegerField(blank=True, null=True)),
                ('duree_spectacle', models.TimeField(blank=True, null=True)),
                ('cachet_ttc', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('mail', models.EmailField(blank=True, max_length=50)),
                ('designation_spectacle', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Devis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(blank=True, max_length=30)),
                ('date_crea', models.DateField()),
                ('objet', models.CharField(blank=True, max_length=50)),
                ('titre_spectacle', models.CharField(blank=True, max_length=50)),
                ('nb_artiste', models.IntegerField(blank=True, null=True)),
                ('nb_technicien', models.IntegerField(blank=True, null=True)),
                ('duree_spectacle', models.TimeField(blank=True, null=True)),
                ('cachet_ttc', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('date_spectacle', models.DateField(blank=True, null=True)),
                ('info_complementaire', models.TextField(blank=True)),
                ('artiste', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='liste.prestation')),
            ],
        ),
    ]
