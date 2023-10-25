from celery import shared_task
from aggregator.models import Article
from aggregator.utils import scrape_articles

@shared_task
def scrape_news():
    articles = scrape_articles('https://example.com/news')
    for article in articles:
        Article.objects.create(title=article['title'], url=article['url'], source='Example News')