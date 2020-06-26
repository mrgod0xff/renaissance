from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction, IntegrityError

from itertools import chain

from .models import Image_long, Image_large
# Create your views here.
def photos(request):
    template_name = 'galerie/galerie.html'
    p = Image_large.objects.filter(statut=True)
    pl = Image_long.objects.filter(statut=True)
    imgach = Image_large.objects.filter(statut=False)[:4]
    imgach1 = Image_long.objects.filter(statut=False)[:4]
    #print(pl)
    archive_list = sorted(chain(imgach, imgach1), key=lambda instance: instance.name)
    result_list = sorted(chain(pl, p), key=lambda instance: instance.name)
    paginator = Paginator(result_list, 6)
    page = request.GET.get('page')
    #print(result_list)
    try:
        result_list = paginator.page(page)
    except PageNotAnInteger:
        result_list = paginator.page(1)
    except EmptyPage:
        result_list = paginator.page(paginator.num_pages)
    context = {
        'title': 'La galerie photo',
        'photol': result_list,
        'archive': archive_list,
        'paginate': True
    }
    return render(request, template_name, context)