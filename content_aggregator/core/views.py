from django.shortcuts import render, get_object_or_404
from aggregator.models import Article

def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)


def article_list_view(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})

def article_detail_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_detail.html', {'article': article, 'url': 'https://blog.georg-nikola.com/'})

def landing_page(request):
    # your code here
    return render(request, 'landing_page.html')