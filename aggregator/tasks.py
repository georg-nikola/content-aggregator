from celery import shared_task
from aggregator.models import aggregation
from aggregator.utils import scrape_aggregations
from aggregator.utils import aggregator

@shared_task

def scrape_news():
    sources = [
        {'url': 'https://example.com/news', 'source': 'Example News'},
        {'url': 'https://anotherexample.com/news', 'source': 'Another Example News'}
    ]
    aggregations = aggregator(sources)
    for aggregation in aggregations:
        aggregation.objects.create(title=aggregation['title'], url=aggregation['url'], source=aggregation['source'])
