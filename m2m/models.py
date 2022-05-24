
from django.db import models

class Publication(models.Model):
    title = models.CharField(max_length=30)
    
    class Meta:
        ordering = ['title']
        
    def __str__(self) -> str:
        return self.title
class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)
    
    
    class meta:
        ordering = ['headline']
        
    def __str__(self) -> str:
        return self.headline