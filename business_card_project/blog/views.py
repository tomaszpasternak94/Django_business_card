from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import BlogArticles

# Create your views here.

def all_blogs(request):
    #order by date (descending), limit to the last 5 in a main blog site
    blog_articles = BlogArticles.objects.order_by('-date')
    content = {
        'articles' : blog_articles
    }
    return render(request,'blog/all_blogs.html', content)

def detail(request, blog_id):
    blog = get_object_or_404(BlogArticles, pk=blog_id)
    content = {
        'blog':blog
    }
    return render(request,'blog/detail.html', content)
