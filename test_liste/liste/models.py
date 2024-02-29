from django.db import models

class Prestation(models.Model):
    artiste = models.fields.CharField(max_length=50)
    titre_spectacle = models.fields.CharField(max_length=50)
    nb_artiste = models.fields.IntegerField(null=True, blank=True)
    nb_technicien = models.fields.IntegerField(null=True, blank=True)
    duree_spectacle = models.fields.TimeField(null=True, blank=True)
    cachet_ttc = models.fields.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    mail = models.fields.EmailField(max_length=50, blank=True)
    designation_spectacle = models.fields.TextField(blank=True)


    def __str__(self):
        return f'{self.artiste}'


class Devis(models.Model):
    numero = models.fields.CharField(max_length=30, blank=True)
    date_crea = models.fields.DateField()
    objet = models.fields.CharField(max_length=50, blank=True)

    artiste = models.ForeignKey(Prestation, null=True, blank=True, on_delete=models.CASCADE)
    titre_spectacle = models.fields.CharField(max_length=50, blank=True)
    nb_artiste = models.fields.IntegerField(null=True, blank=True)
    nb_technicien = models.fields.IntegerField(null=True, blank=True)
    duree_spectacle = models.fields.TimeField(null=True, blank=True)
    cachet_ttc = models.fields.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    date_spectacle = models.fields.DateField(null=True, blank=True)

    info_complementaire = models.fields.TextField(blank=True)


    def __str__(self):
        return f'{self.numero}'


class Facturation(models.Model):
    qte = models.fields.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    prix = models.fields.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    total = models.fields.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    apply_tax = models.fields.BooleanField(default=True, blank=True)
    tax = models.fields.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'{self.total}'

