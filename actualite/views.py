from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction, IntegrityError
from django.core.mail import send_mail
from renaissance.settings import EMAIL_HOST_USER
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import uuid
# Create your views here.
from .models import Article, Categorie, Nouveaute
from titrologie.models import Revue
from .forms import CommentForm


def actualites(request):
    articles = Article.objects.all()
    cartego  = Categorie.objects.all()
    revue = Revue.objects.all()[:5]

    paginator = Paginator(articles, 4)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    context = {
        'title': 'Actualité Ivoirienne',
        'articles': articles,
        'category': cartego,
        'revue': revue,
        'paginate': True
    }

    return render(request, 'actualite/listing.html', context)


@transaction.atomic
def see_more(request, article_id):
    template_name = 'actualite/see-more.html'
    article = get_object_or_404(Article, pk=article_id)
    last_art = Article.objects.all()[:3]
    last_news = Nouveaute.objects.all()[:3]
    comments = article.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            nom = comment_form.cleaned_data['nom']
            email = comment_form.cleaned_data['email']
            message = comment_form.cleaned_data['message']
            # Créer un objet Commentaire mais ne pas encore enregistrer dans la base de données
            new_comment = comment_form.save(commit=False)
            # Attribuer le message actuel au commentaire
            new_comment.post = article
            guest_name = new_comment.nom
            guest_email = new_comment.email
            guest_message = new_comment.message
            subject = "Notification sur Actualité"
            print(new_comment.id)
            context = {
                'id': new_comment.id,
                'author': guest_name,
                'message': guest_message,
                'article': article
            }
            msg_html = render_to_string('actualite/email.html', context)
            plain_message = strip_tags(msg_html)
            # Enregistrez le commentaire dans la base de données
            send_mail(subject, plain_message, EMAIL_HOST_USER, ['kouameaugui@gmail.com'], fail_silently = False, html_message=msg_html)
            new_comment.save()
            
    else:
        comment_form = CommentForm()
    data = {
                'article_id': str(article.id),
                'article_titre': article.titre,
                'last': last_art,
                'l_new': last_news,
                'content': article.content,
                'type': article.genre,
                'thumbnail': article.image,
                'comments': comments,
                'new_comment': new_comment,
                "comment_form": comment_form
            }
    for row in data:
        if isinstance(row, str):
            for item in row.split(','):
                data[item].add()
        else:
            data['numbers'].add()

    return render(request, template_name, data)