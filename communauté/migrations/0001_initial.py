# Generated by Django 3.2.8 on 2024-05-25 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Membre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('date_naissance', models.DateField()),
                ('adresse', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('date_inscription', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('budget', models.FloatField()),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Versement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.FloatField()),
                ('date_versement', models.DateField()),
                ('beneficiaires', models.CharField(max_length=255)),
                ('membre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communauté.membre')),
            ],
        ),
        migrations.CreateModel(
            name='Reunion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('date_creation', models.DateField(auto_now_add=True)),
                ('chef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reunions_chef', to='communauté.membre')),
                ('membres', models.ManyToManyField(related_name='reunions', to='communauté.Membre')),
            ],
        ),
        migrations.CreateModel(
            name='Financement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.FloatField()),
                ('date', models.DateField()),
                ('membre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communauté.membre')),
                ('projet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communauté.projet')),
            ],
        ),
        migrations.CreateModel(
            name='Cotisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annee', models.IntegerField()),
                ('montant', models.FloatField()),
                ('date_paiement', models.DateField()),
                ('membre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communauté.membre')),
                ('reunion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='communauté.reunion')),
            ],
        ),
    ]
