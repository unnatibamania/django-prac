from django.shortcuts import render

# Create your views here.
import django.http

def students(request):
    students = [{
        'id': 1,
        'name': 'John',
        'age': 20,
        'city': 'New York'
    },
    {   
        'id': 2,
        'name': 'Jane',
        'age': 21,
        'city': 'Los Angeles'
    },
   ]
    return django.http.HttpResponse("<h2>Hello World</h2>")

