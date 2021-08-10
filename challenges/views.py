from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.


def index(Request):
    return HttpResponse("It's an index page!")


def fun(Request, string):
    if string == "404":
        return HttpResponseNotFound("It's not valid.")
    return HttpResponse(f'wow {string}')
