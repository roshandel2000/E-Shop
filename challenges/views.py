from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.


def index(request):
    return HttpResponse("It's an index page!")


def fun(request, string):
    if string == "404":
        return HttpResponseNotFound("It's not valid.")
    return HttpResponse(f'wow {string}')


def fun_by_number(request, num):
    return HttpResponseRedirect(reverse("fun", args=[f'{num}redirect']))
    # return HttpResponseRedirect(f'/challenges/{num}redirect')
    # return HttpResponse(f'It\'s a number: {num}')