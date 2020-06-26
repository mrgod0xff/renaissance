from django.shortcuts import render
from .forms import AdhesionForm
from .models import Adhesion
# Create your views here.

def addUser(request):
    template_name = 'adhesion/form-adherant.html'
    if request.method == 'POST':
        form = AdhesionForm(request.POST)
        if form.is_valid():
            nom_et_prenom = form.cleaned_data['nom_et_prenom']
            numero_de_telephone = form.cleaned_data['numero_de_telephone']
            date_de_naissance = form.cleaned_data['date_de_naissance']
            email = form.cleaned_data['email']
            domicile = form.cleaned_data['domicile']
            profession = form.cleaned_data['profession']
            pays_de_residence = form.cleaned_data['pays_de_residence']
            lieu_de_naissance = form.cleaned_data['lieu_de_naissance']
            ville_de_residence = form.cleaned_data['ville_de_residence']

            adherant = Adhesion.objects.filter(email=email)

            if not adherant.exists():
                adherant = Adhesion.objects.create(
                    nom_et_prenom=nom_et_prenom,
                    numero_de_telephone=numero_de_telephone,
                    date_de_naissance=date_de_naissance,
                    email=email,
                    domicile=domicile,
                    profession=profession,
                    pays_de_residence=pays_de_residence,
                    lieu_de_naissance=lieu_de_naissance,
                    ville_de_residence=ville_de_residence
                )
                form.save()
            else:
                adherant = adherant.first()
        
        else:
            context ={
                'errors': form.errors.items()
                }
    else:
        form = AdhesionForm()
    context = {
        'form':form
        }
    return render(request, template_name, context)

