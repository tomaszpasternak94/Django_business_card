from django.shortcuts import render
from .models import BlogArticles

# Create your views here.

def all_blogs(request):
    blog_articles = BlogArticles.objects.all()
    content = {
        'articles' : blog_articles
    }
    return render(request,'blog/all_blogs.html', content)