from django.shortcuts import render
from .models import BlogArticles

# Create your views here.

def all_blogs(request):
    #order by date (descending), limit to the last 5 in a main blog site
    blog_articles = BlogArticles.objects.order_by('-date')[:5]
    content = {
        'articles' : blog_articles
    }
    return render(request,'blog/all_blogs.html', content)