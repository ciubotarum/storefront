from django.shortcuts import render

# Create your views here.
# a function that take a request and give a response
# request handler

from django.http import HttpResponse

def calculate():
    x = 1
    y = 2
    return x


def say_hello(request):
    # we can pull data from db
    # transform
    # send email
    # return HttpResponse('Hello World') 
    x = calculate()
    return render(request, 'hello.html', {'name': 'Mosh'})