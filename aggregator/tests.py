from django.test import TestCase
from django.urls import reverse
from .models import Article

class ArticleTestCase(TestCase):
    def setUp(self):
        Article.objects.create(title='Test Article', url='https://blog.georg-nikola.com/', source='Example News')

    def test_article_list_view(self):
        response = self.client.get(reverse('article_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Article')

    def test_article_detail_view(self):
        article = Article.objects.get(title='Test Article')
        response = self.client.get(reverse('article_detail', args=[article.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Article')
        self.assertContains(response, 'https://blog.georg-nikola.com/')
        # self.assertContains(response, 'Example News')