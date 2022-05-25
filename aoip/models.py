
from django.db import models



class Sauce(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Sandwich(models.Model):
    name = models.CharField(max_length=100)
    sauces = models.ManyToManyField(Sauce)

    def __str__(self):
        return self.name





class IpList(models.Model):
    ip = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.ip


class AllowOrigin(models.Model):
    headline = models.CharField(max_length=100)
    ips = models.ManyToManyField(IpList, related_name="ip_lists")

    class meta:
        ordering = ['headline']

    def __str__(self) -> str:
        return self.headline
