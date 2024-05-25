from django.db import models

class Membre(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    adresse = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    date_inscription = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Reunion(models.Model):
    nom = models.CharField(max_length=100)
    date_creation = models.DateField(auto_now_add=True)
    chef = models.ForeignKey(Membre, on_delete=models.CASCADE, related_name='reunions_chef')
    membres = models.ManyToManyField(Membre, related_name='reunions')

    def __str__(self):
        return self.nom

class Cotisation(models.Model):
    annee = models.IntegerField()
    montant = models.FloatField()
    date_paiement = models.DateField()
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE)
    reunion = models.ForeignKey(Reunion, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Cotisation de {self.membre} pour l'année {self.annee}"

class Projet(models.Model):
    description = models.TextField()
    budget = models.FloatField()
    date_debut = models.DateField()
    date_fin = models.DateField()

    def __str__(self):
        return self.description

class Financement(models.Model):
    montant = models.FloatField()
    date = models.DateField()
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.membre} a financé {self.projet} avec {self.montant}"

class Versement(models.Model):
    montant = models.FloatField()
    date_versement = models.DateField()
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE)
    beneficiaires = models.CharField(max_length=255)

    def __str__(self):
        return f"Versement de {self.montant} pour {self.membre}"
