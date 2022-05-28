from django.db import models
from django.contrib.auth import get_user_model
#usermo
User = get_user_model()

class IpList(models.Model):
    ip = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.ip
    
    
class AllowOrigin(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ip_list = models.ManyToManyField(IpList)
    is_active = models.BooleanField(default=False)
    
    
    def __str__(self) -> str:
        return self.user.username
