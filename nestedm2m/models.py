
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