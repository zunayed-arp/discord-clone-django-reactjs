from ast import GtE, LtE
from calendar import day_abbr, month
from operator import contains, lt
import re
from django.shortcuts import render
from .models import Student, Teacher
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

def student_list03(request):
    obj = Student.objects.filter(Q(surname__startswith='ahmed') & Q(firstname__startswith='shamim'))
    print(obj)
    print(obj.query)
    print(connection.queries)
    return render(request, 'output.html', {'posts': obj})

#part04 UNION Query ORM
def student_list04(request):
    obj = Student.objects.all().values_list("firstname").union(Teacher.objects.all().values('surname'))
    print(obj)
    print(obj.query)
    print(connection.queries)
    return render(request, 'output.html', {'posts': obj})


#part04 UNION Query ORM
#gt
#gte
#lt
#lte
def student_list051(request):
    # obj = Student.objects.exclude(age=30) & Student.objects.exclude(firstname__startswith='shamim')
    obj = Student.objects.exclude(age__gt=30)
    print(obj.query)
    print(connection.queries)
    return render(request, 'output.html', {'posts': obj})

def student_list052(request):
    obj = Student.objects.filter(~Q(age__gt=30) & ~Q(surname__startswith='ahmed'))
    print(obj.query)
    print(connection.queries)
    return render(request, 'output.html', {'posts': obj})

#part06
def student_list06(request):
    obj = Student.objects.filter(classroom=6).only('firstname')
    print(obj.query)
    print(connection.queries)
    return render(request, 'output.html', {'data': obj})


#part07
def student_list07(request):
    obj = Student.objects.all()
    # posts = Student.objects.raw("SELECT * FROM students_student WHERE age=35 ")
    
    # for s in Student.objects.raw("SELECT * FROM students_student WHERE age=35"):
    #     print(s)
    ##mapping 
    # student_mapping = {'fname':'firstname','sname':'surname'}
    # objs = Student.objects.raw("SELECT * FROM students_student",translations=student_mapping)
    # print(objs)
    sql = "SELECT * FROM students_student"
    posts = Student.objects.raw(sql)[:2]
    
    # print(obj.query)
    # print(connection.queries)
    # print(obj)
    return render(request, 'output.html', {'data': obj})


#part08


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]



def student_list(request):
    #bypassing orm 
    cursor = connection.cursor()
    # cursor.execute("SELECT * FROM students_student")
    cursor.execute("SELECT * FROM students_student WHERE age > 20")
    # r = cursor.fetchone()
    r = dictfetchall(cursor)
    print(r)
    print(connection.queries)
    return render(request, 'output.html', {'data': r})

# exact
# iexact
# contains
# icontains
# in 
# gt 
# lt
# lte
# startswith
# istartswith
# endswith
# iendswith
# range
# year
# month
# day
# week_day
# isnull
# search
# regex
# iregex






