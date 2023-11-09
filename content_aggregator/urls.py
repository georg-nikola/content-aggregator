from django.contrib import admin
from django.urls import path, include

from content_aggregator.core import views as core_views
from content_aggregator.core.views import aggregation_list_view, aggregation_detail_view, landing_page, error_404, index

urlpatterns = [
    path("", index),
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('aggregations/', aggregation_list_view, name='aggregation_list'),
    path('aggregations/<int:pk>/', aggregation_detail_view, name='aggregation_detail'),
    path('', landing_page, name='landing_page'),
    path('aggregations/<int:pk>/', error_404, name='error_404'),
]