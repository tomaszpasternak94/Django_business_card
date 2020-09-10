from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
    stack = models.TextField()

    def __str__(self):
        return self.title

class Skills(models.Model):
    skill = models.CharField(max_length=200)

    def __str__(self):
        return self.skill