from django.db import models

# Create your models here.

class BlogArticles(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.title
