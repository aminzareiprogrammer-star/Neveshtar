from django.shortcuts import render
from blog.models import Article
from blog.models import Category


def categories(request):
    return {
        'categories': Category.objects.all()
    }
def recent(request):
    articles = Article.objects.filter(
        status=True
    ).order_by('-created')[:5]

    return {
        'recent': articles
    }