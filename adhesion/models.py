from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

#from django.core.validators import RegexValidator
import uuid


# Create your models here.
class Adhesion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom_et_prenom  = models.CharField(max_length=100)
    genre  = models.CharField(max_length=100)
    numero_de_telephone = PhoneNumberField(null=False, blank=False, unique=True)
    date_de_naissance = models.DateField()
    email = models.EmailField(max_length=100)
    domicile = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    pays_de_residence = CountryField()
    lieu_de_naissance = models.CharField(max_length=100)
    ville_de_residence = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_et_prenom
