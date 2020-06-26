from django.shortcuts import render, redirect
from django.http import HttpResponse

from  accueil.models import Biographie, Vision, Objectif, Priorite, Strategie
from  titrologie.models import Revue
from  actualite.models import Article
# Create your views here.
def home_page(request):
    bio = Biographie.objects.all()[:1]
    vision = Vision.objects.all()[:1]
    objectif = Objectif.objects.all()[:1]
    priorite = Priorite.objects.all()[:1]
    strategie = Strategie.objects.all()[:1]
    titrologies = Revue.objects.all()[:4]
    actualites  = Article.objects.filter(active=True)[:4]
    context = {
        'bio': bio,
        'vision': vision,
        'objectif': objectif,
        'priorite': priorite,
        'strategie': strategie,
        'titrologs': titrologies,
        'actus': actualites
    }
    return render(request, "home_page.html", context)