import requests
from bs4 import BeautifulSoup

def scrape_articles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = []
    for article in soup.find_all('article'):
        title = article.find('h2').text.strip()
        url = article.find('a')['href']
        articles.append({'title': title, 'url': url})
    return articles