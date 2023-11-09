from django.contrib import admin
from django.urls import path, include

from content_aggregator.core import views as core_views
from content_aggregator.core.views import article_list_view, article_detail_view, landing_page, error_404, index

urlpatterns = [
    path("", index),
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('articles/', article_list_view, name='article_list'),
    path('articles/<int:pk>/', article_detail_view, name='article_detail'),
    path('', landing_page, name='landing_page'),
    path('articles/<int:pk>/', error_404, name='error_404'),
]
