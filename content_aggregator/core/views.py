from django.shortcuts import render, get_object_or_404
from aggregator.models import aggregation
from django.http import Http404

def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)


def aggregation_list_view(request):
    aggregations = aggregation.objects.all()
    return render(request, 'aggregation_list.html', {'aggregations': aggregations})

def aggregation_detail_view(request, pk):
    aggregation = get_object_or_404(aggregation, pk=pk)
    return render(request, 'aggregation_detail.html', {'aggregation': aggregation, 'url': 'https://blog.georg-nikola.com/'})

def error_404(request, pk):
    if not aggregation.objects.filter(pk=pk).exists():
        raise Http404("aggregation does not exist")

def home_view(request):
    context = {
        "title": "Content Aggregator",
    }
    return render(request, "index.html", context)