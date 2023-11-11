from celery import shared_task
from aggregator.models import aggregation
from aggregator.utils import scrape_aggregations
import requests
from bs4 import BeautifulSoup

@shared_task
def scrape_news():
    sources = [
        {'url': 'https://example.com/news', 'source': 'Example News'},
        {'url': 'https://anotherexample.com/news', 'source': 'Another Example News'}
    ]
    aggregations = scrape_aggregations(sources)
    for aggregation in aggregations:
        aggregation.objects.create(title=aggregation['title'], url=aggregation['url'], source=aggregation['source'])

@shared_task
def scrape_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.title.string
    new_aggregation = aggregation.objects.create(title=title, url=url, source='Unknown')
    return new_aggregation
