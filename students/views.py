import re
from django.shortcuts import render
from .models import Student
from django.db import connection
from django.db.models import Q

#part01
def student_list_(request):
    obj = Student.objects.all()
    print(obj)
    print(obj.query)
    print(connection.queries)
    return render(request, 'output.html', {'posts': obj})
#part02
#OROperation
def student_list__(request):
    # obj = Student.objects.filter(surname__startswith='ahmed') | Student.objects.filter(surname__startswith='habib')
    # obj = Student.objects.filter(Q(surname__startswith='ahmed') | Q(surname__startswith='habib') | Q(surname__startswith='haldar'))
    obj = Student.objects.filter(Q(surname__startswith='ahmed') | ~Q(surname__startswith='habib') | Q(surname__startswith='haldar'))
    print(obj)
    print(obj.query)
    print(connection.queries)
    return render(request, 'output.html', {'posts': obj})

#part03
#andoperation
def student_list____(request):
    # obj = Student.objects.filter(classroom=6) & Student.objects.filter(firstname__startswith='shamim')
    # obj = Student.objects.exclude(classroom=6) & Student.objects.filter(firstname__startswith='shamim')
   
    obj = Student.objects.filter(classroom=6) & Student.objects.filter(age=30)
    print(obj)
    print(obj.query)
    print(connection.queries)
    return render(request, 'output.html', {'posts': obj})

def student_list(request):
    obj = Student.objects.filter(Q(surname__startswith='ahmed') & Q(firstname__startswith='shamim'))
    print(obj)
    print(obj.query)
    print(connection.queries)
    return render(request, 'output.html', {'posts': obj})
