from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction, IntegrityError
# Create your views here.

from .models import Revue

def list_revue(request):
    f = Revue.objects.all()
    paginator = Paginator(f, 4)
    page = request.GET.get('page')
    try:
        f = paginator.page(page)
    except PageNotAnInteger:
        f = paginator.page(1)
    except EmptyPage:
        f = paginator.page(paginator.num_pages)
    context = {
        'title': 'Revue de presse ivoirienne',
        'f': f,
        'paginate': True
    }
    return render(request, 'titrologie/revue-list.html', context)
