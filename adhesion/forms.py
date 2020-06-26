import datetime
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from phonenumber_field.formfields import PhoneNumberField
from django_countries.fields import CountryField
from bootstrap_datepicker_plus import DatePickerInput
#from .widgets import FengyuanChenDatePickerInput

GENRE = (
        ('', 'Choisir...'),
        ('M', 'Masculin'),
        ('F', 'Feminin')
    )

class AdhesionForm(forms.Form):
    nom_et_prenom = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nom & Prenom'}))
    numero_de_telephone = PhoneNumberField()
    date_de_naissance = forms.DateField(
        widget=DatePickerInput(format='%m/%d/%Y')
    )
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Adresse electronique'}))
    domicile = forms.CharField(
        label='Adresse',
        widget=forms.TextInput(attrs={'placeholder': 'Rue 26, abidjan'}),
        )
    profession = forms.CharField(
        label='Profession',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    pays_de_residence = CountryField().formfield()
    genre = forms.ChoiceField(choices=GENRE)
    lieu_de_naissance = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'DEBO S/P Zoukougbeu'}),
    )
    ville_de_residence = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('nom_et_prenom', css_class='form-group col-md-4 mb-0'),
                Column('email', css_class='form-group col-md-4 mb-0'),
                Column('numero_de_telephone', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('genre', css_class='form-group col-md-4 mb-0'),
                Column('date_de_naissance', css_class='form-group col-md-4 mb-0'),
                Column('lieu_de_naissance', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            'domicile',
            Row(
                Column('ville_de_residence', css_class='form-group col-md-4 mb-0'),
                Column('pays_de_residence', css_class='form-group col-md-4 mb-0'),
                Column('profession', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Soumettre')
        )