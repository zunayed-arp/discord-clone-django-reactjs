import re
from django.shortcuts import render
from .models import Student
from django.db import connection
from django.db.models import Q


def student_list_(request):
    obj = Student.objects.all()
    print(obj)
    print(obj.query)
    print(connection.queries)
    return render(request, 'output.html', {'posts': obj})

def student_list(request):
    obj = Student.objects.filter(surname__startswith='ahmed') | Student.objects.filter(surname__startswith='habib')
    print(obj)
    print(obj.query)
    print(connection.queries)
    return render(request, 'output.html', {'posts': obj})
