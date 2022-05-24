
from django.db import models
from pytz import timezone


class Teacher(models.Model):
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    
    def __str__(self):
        return self.firstname
    
class Student(models.Model):
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    classroom = models.IntegerField()
    teacher = models.CharField(max_length=100)
    
    def __str__(self):
        return self.firstname
    
    
#proxy model 

class BookContent(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    
class BookOrders(BookContent):
    # objects = NewManager()
    class Meta:
        proxy=True
        ordering = ['created']

    def created_on(self):
        return timezone.now()-self.created





class Books(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    
class ISBN(Books):
    """_summary_

    Args:
        Books (_type_): _description_
    """   
    books_ptr = models.OneToOneField(
        Books,on_delete=models.CASCADE,
        parent_link=True,
        primary_key=True,
    )
    ISBN = models.TextField()




#abstract Model
class BaseItem(models.Model):
    title = models.CharField(max_length=255)
    created= models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        ordering = ['title']
        
class ItemA(BaseItem):
    content = models.TextField()
    
    class Meta(BaseItem.Meta):
        ordering = ['-created']
        
class ItemB(BaseItem):
    file = models.FileField(upload_to='files')


class ItemC(BaseItem):
    file = models.FileField(upload_to='images')
    

class ItemD(BaseItem):
    slug = models.SlugField(max_length=255,unique=True)
