from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    #indicate the cahnge frequency of post pages and relevance in the website
    changefreq = 'weekly'
    priority = 0.9


    #return the queryset of objects to include in the sitemap
    def items(self):
        return Post.published.all()
    
    #recieve each object returned by items and returns the last time the object was modified
    def lastmod(self, obj):
        return obj.updated