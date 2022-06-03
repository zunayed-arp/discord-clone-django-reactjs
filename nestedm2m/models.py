
from django.db import models
from django.contrib.auth.models import User


class IpList(models.Model):
    ip = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.ip


class AllowOrigin(models.Model):
    ip_list = models.ManyToManyField(IpList)

    def __str__(self) -> str:
        return self.ip_list.ip
    
    
    
class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    directions = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.name
