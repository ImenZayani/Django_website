from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    return render (request,'index.html')
    #template = loader.get_template('index.html')
    #return HttpResponse(template.render({},request))

def about(request: HttpRequest) -> HttpResponse:
    return render (request,'about.html')


def contact(request: HttpRequest) -> HttpResponse:
    return render (request,'contact.html')